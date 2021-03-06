"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.protobuf.wrappers_pb2
import grpc

class TimeStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    now: grpc.UnaryUnaryMultiCallable[
        google.protobuf.wrappers_pb2.StringValue,
        google.protobuf.wrappers_pb2.StringValue]
    """It returns an ISO 8601 string."""


class TimeServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def now(self,
        request: google.protobuf.wrappers_pb2.StringValue,
        context: grpc.ServicerContext,
    ) -> google.protobuf.wrappers_pb2.StringValue:
        """It returns an ISO 8601 string."""
        pass


def add_TimeServicer_to_server(servicer: TimeServicer, server: grpc.Server) -> None: ...
