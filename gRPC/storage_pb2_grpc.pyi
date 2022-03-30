"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.protobuf.wrappers_pb2
import grpc
import storage_pb2

class StorageStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    put: grpc.UnaryUnaryMultiCallable[
        storage_pb2.Pair,
        google.protobuf.wrappers_pb2.StringValue]

    get: grpc.UnaryUnaryMultiCallable[
        google.protobuf.wrappers_pb2.StringValue,
        storage_pb2.Pair]


class StorageServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def put(self,
        request: storage_pb2.Pair,
        context: grpc.ServicerContext,
    ) -> google.protobuf.wrappers_pb2.StringValue: ...

    @abc.abstractmethod
    def get(self,
        request: google.protobuf.wrappers_pb2.StringValue,
        context: grpc.ServicerContext,
    ) -> storage_pb2.Pair: ...


def add_StorageServicer_to_server(servicer: StorageServicer, server: grpc.Server) -> None: ...
