from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging
from os import cpu_count
from typing import Dict
from google.protobuf.message import Message

from google.protobuf.wrappers_pb2 import StringValue
import grpc

from storage_pb2 import Pair
from storage_pb2_grpc import StorageServicer, add_StorageServicer_to_server

from time_pb2_grpc import TimeServicer, add_TimeServicer_to_server


class Time(TimeServicer):

	def now(self, request: StringValue,
	        context: grpc.ServicerContext) -> StringValue:
		dt = datetime.utcnow().isoformat() + 'Z'
		logging.debug(dt)
		return StringValue(value=dt)


class Storage(StorageServicer):

	def __init__(self) -> None:
		self._storage: Dict[str, str] = {}
		return

	def put(self, request: Pair, context: grpc.ServicerContext) -> StringValue:
		self._storage[request.key] = request.value
		logging.debug(request)
		return StringValue(value=request.value)

	def get(self, request: StringValue, context: grpc.ServicerContext) -> Pair:
		if request.value not in self._storage:
			context.abort(grpc.StatusCode.NOT_FOUND,
			              f"{request.value} not exists")

		item = Pair(key=request.value, value=self._storage[request.value])
		logging.debug(item)
		return item


class OAuthInterceptor(grpc.ServerInterceptor):

	def __init__(self) -> None:

		def abort(_ignored_request: Message, context: grpc.ServicerContext):
			context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid TOKEN")

		self._abortion = grpc.unary_unary_rpc_method_handler(abort)
		return

	def intercept_service(self, continuation, handler_call_details):

		authorized_tokens = ['secret-token']

		metadata = handler_call_details.invocation_metadata

		if next((v.split()[-1] for k, v in metadata if k == 'authentication'),
		        None) not in authorized_tokens:
			return self._abortion

		return continuation(handler_call_details)


def main(port=50051):
	server = grpc.server(ThreadPoolExecutor(cpu_count()),
	                     interceptors=[OAuthInterceptor()])
	add_StorageServicer_to_server(Storage(), server)
	add_TimeServicer_to_server(Time(), server)
	server.add_insecure_port(f"[::]:{port}")
	server.start()

	return server


if __name__ == "__main__":
	logging.basicConfig(
	    level=logging.DEBUG,
	    format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
	main().wait_for_termination()
