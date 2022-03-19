
PROTO_SRC=proto/storage.proto
PROTO_TARGET=proto/storage_pb2.py proto/storage_pb2_grpc.py
MYPY_STUB_TARGET=proto/storage_pb2.pyi proto/storage_pb2_grpc.pyi

install: $(PROTO_TARGET) $(MYPY_STUB_TARGET)

proto/%.py: $(PROTO_SRC)
	python3 -m grpc_tools.protoc -I proto -I proto/googleapis --python_out proto --grpc_python_out proto proto/storage.proto

proto/%.pyi: $(PROTO_SRC)
	python3 -m grpc_tools.protoc -I proto -I proto/googleapis --mypy_out proto --mypy_grpc_out proto proto/storage.proto

clean:
	$(RM) $(PROTO_TARGET) $(MYPY_STUB_TARGET)
