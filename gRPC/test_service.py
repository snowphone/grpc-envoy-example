#!/usr/bin/env python3
import re

from google.protobuf.wrappers_pb2 import StringValue
import grpc
import pytest

from storage_pb2 import Pair
from storage_pb2_grpc import StorageStub
from time_pb2_grpc import TimeStub

PORT=50052

@pytest.fixture(scope="session")
def serv():
	import server
	s = server.main(PORT)
	yield s
	s.stop(0)


@pytest.fixture(scope="session")
def md():
	# https://groups.google.com/g/grpc-io/c/fFXbIXphudw
	# cred = grpc.access_token_call_credentials("secret-token")
	token = "secret-token"
	return tuple({"authentication": f"Bearer {token}"}.items())

@pytest.fixture
def storage_stub():
	with grpc.insecure_channel(f"localhost:{PORT}") as channel:
		 yield StorageStub(channel)

@pytest.fixture
def time_stub():
	with grpc.insecure_channel(f"localhost:{PORT}") as channel:
		 yield TimeStub(channel)


def test_storage(serv: grpc.Server, storage_stub: StorageStub, md):

	cred = grpc.access_token_call_credentials("secret-token")

	pair = Pair(key="hi", value="bixby")

	ret, call = storage_stub.put.with_call(pair, credentials=cred, metadata=md)
	assert call.code() == grpc.StatusCode.OK
	assert ret == StringValue(value=pair.value)

	ret, call = storage_stub.get.with_call(StringValue(value=pair.key),
								   metadata=md)
	assert call.code() == grpc.StatusCode.OK
	assert ret == pair


def test_storage_without_auth(serv: grpc.Server, storage_stub: StorageStub):
	pair = Pair(key="hi", value="bixby")

	with pytest.raises(grpc.RpcError) as e:
		storage_stub.put.with_call(pair)
		assert e.value.code() == grpc.StatusCode.UNAUTHENTICATED


def test_time(serv: grpc.Server, time_stub: TimeStub, md):
	response, call = time_stub.now.with_call(StringValue(value=''), metadata=md)

	assert call.code() == grpc.StatusCode.OK
	pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([.]\d+)?Z"
	assert re.match(pattern, response.value)

def test_time_without_auth(serv: grpc.Server, time_stub: TimeStub):
	with pytest.raises(grpc.RpcError) as e:
		time_stub.now(StringValue(value=''))
		assert e.value.code() == grpc.StatusCode.UNAUTHENTICATED
