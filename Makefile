
PROTO_SRC=proto/storage.proto
PROTO_TARGET=proto/storage_pb2.py proto/storage_pb2_grpc.py gRPC/storage_pb2.py gRPC/storage_pb2_grpc.py
MYPY_STUB_TARGET=proto/storage_pb2.pyi proto/storage_pb2_grpc.pyi
PROTO_DESCRIPTOR=envoy_proxy/storage.desc

install: $(PROTO_TARGET) $(MYPY_STUB_TARGET) $(PROTO_DESCRIPTOR)

up:
	docker-compose up --build -d --scale storage_server=4

proto/%.py: $(PROTO_SRC)
	python3 -m grpc_tools.protoc \
		-I proto \
		-I proto/googleapis \
		--include_imports \
		--descriptor_set_out $(PROTO_DESCRIPTOR) \
		--python_out gRPC \
		--grpc_python_out gRPC \
		proto/storage.proto

proto/%.pyi: $(PROTO_SRC)
	python3 -m grpc_tools.protoc \
		-I proto \
		-I proto/googleapis \
		--mypy_out gRPC \
		--mypy_grpc_out gRPC \
		proto/storage.proto

clean:
	$(RM) $(PROTO_TARGET) $(MYPY_STUB_TARGET)
