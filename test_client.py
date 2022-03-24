from google.protobuf.wrappers_pb2 import StringValue
import re
from gRPC.server import Storage
import grpc
from gRPC.storage_pb2 import Pair
from gRPC.storage_pb2_grpc import StorageStub, add_StorageServicer_to_server
import pytest
from concurrent.futures import ThreadPoolExecutor

PORT=54321

@pytest.fixture(scope="module")
def server():
	server = grpc.server(ThreadPoolExecutor(max_workers=1), maximum_concurrent_rpcs=5)
	add_StorageServicer_to_server(Storage(), server)
	server.add_insecure_port(f"[::]:{PORT}")
	server.start()

	yield server

	server.stop(None)

@pytest.fixture
def client():
	chan = grpc.insecure_channel(f"localhost:{PORT}")
	stub = StorageStub(chan)
	yield stub
	chan.close()

def test_time(server: grpc.Server, client: StorageStub):
	response = client.time(StringValue()).value
	assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([.]\d+)?Z", response) is not None

def test_key_value(server: grpc.Server, client: StorageStub):
	key = "Hello"
	value = "world!"
	response = client.put(Pair(key=key, value=value))

	assert response.value == value

	assert client.get(StringValue(value=key)) == Pair(key=key, value=value)

	with pytest.raises(grpc.RpcError) as e:
		client.get(StringValue(value="This must not exist"))
		assert e.value.code() == grpc.StatusCode.NOT_FOUND
		

