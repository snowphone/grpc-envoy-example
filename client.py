from toolz.curried import pipe
import logging

from google.protobuf.wrappers_pb2 import StringValue
import grpc

from proto.storage_pb2 import Pair
from proto.storage_pb2_grpc import StorageStub


def main():
	with grpc.insecure_channel("localhost:50051") as channel:
		stub = StorageStub(channel)

		result = stub.put(Pair(key="hello", value="world"))
		logging.info(result)

		pipe(StringValue(value="hello"), stub.get, logging.info)

		try:
			pipe(StringValue(value="not hello"), stub.get, logging.info)
		except grpc.RpcError as e:
			logging.warning(e.code())
			logging.warning(e.details())
	return


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	main()
