#!/usr/bin/env python3
import logging

from google.protobuf.wrappers_pb2 import StringValue
import grpc
from toolz.curried import pipe

from proto.storage_pb2 import Pair
from proto.storage_pb2_grpc import StorageStub


def main():
	with grpc.insecure_channel("localhost:50051") as channel:
		stub = StorageStub(channel)

		while True:
			try:
				job, tail = parse_command()
				if job == "get":
					pipe(StringValue(value=tail), stub.get, logging.info)
				else:
					k, v = tail
					pipe(Pair(key=k, value=v), stub.put, logging.info)
			except grpc.RpcError as e:
				logging.warning(e.code())
				logging.warning(e.details())
			except RuntimeError:
				continue
			except ValueError:
				continue
			except EOFError:
				break
			except KeyboardInterrupt:
				break
	return


def parse_command():
	cmd, tail = input("Input: get <key> | set <key>:<value>\n").split(maxsplit=1)

	if cmd == "get":
		return cmd, tail
	elif cmd == "set":
		return cmd, tail.split(':', maxsplit=1)
	else:
		raise RuntimeError()


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
	main()
