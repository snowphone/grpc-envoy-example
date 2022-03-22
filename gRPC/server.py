from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone, tzinfo
import logging
from os import cpu_count
from time import ctime, sleep
from typing import Dict

from google.protobuf.wrappers_pb2 import StringValue
import grpc

from storage_pb2 import Pair
from storage_pb2_grpc import StorageServicer, add_StorageServicer_to_server

class Storage(StorageServicer):
	def __init__(self) -> None:
		self._storage: Dict[str, str] = {}
		return
	
	def put(self, request: Pair, context: grpc.ServicerContext) -> StringValue:
		self._storage[request.key] = request.value
		return StringValue(value=request.value)

	def get(self, request: StringValue, context: grpc.ServicerContext) -> Pair:
		if request.value not in self._storage:
			context.abort(grpc.StatusCode.NOT_FOUND, f"{request.value} not exists")

		return Pair(key=request.value, value=self._storage[request.value])

	def time(self, request: StringValue, context: grpc.ServicerContext) -> StringValue:
		dt = str(datetime.now(timezone.utc)).replace("+00:00", "Z")
		logging.info(dt)
		return StringValue(value=dt)

def main():
	server = grpc.server(ThreadPoolExecutor(cpu_count()))
	add_StorageServicer_to_server(Storage(), server)
	server.add_insecure_port("[::]:50051")
	server.start()

	while True:
		sleep(3600)

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
	main()
