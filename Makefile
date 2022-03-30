PROTO_SRC_BASE=storage.proto time.proto
PROTO_SRC=$(addprefix proto/,$(PROTO_SRC_BASE))
PROTO_TARGET=$(addprefix gRPC/, $(PROTO_SRC_BASE:.proto=_pb2.py) $(PROTO_SRC_BASE:.proto=_pb2_grpc.py))
MYPY_STUB_TARGET=$(PROTO_TARGET:.py=.pyi)
PROTO_DESCRIPTOR=envoy_proxy/services.desc

CMD=python3 -m grpc_tools.protoc
FLAGS=-I proto -I proto/googleapis

install: $(PROTO_TARGET) $(MYPY_STUB_TARGET) $(PROTO_DESCRIPTOR)

up:
	docker-compose up --build -d --scale storage_server=4

gRPC/%_pb2_grpc.py: proto/%.proto
	$(CMD) \
		$(FLAGS) \
		--grpc_python_out gRPC \
		$^

gRPC/%_pb2_grpc.pyi: proto/%.proto
	$(CMD) \
		$(FLAGS) \
		--mypy_grpc_out gRPC \
		$^

gRPC/%_pb2.py: proto/%.proto
	$(CMD) \
		$(FLAGS) \
		--python_out gRPC \
		$^

gRPC/%_pb2.pyi: proto/%.proto
	$(CMD) \
		$(FLAGS) \
		--mypy_out gRPC \
		$^

$(PROTO_DESCRIPTOR): $(PROTO_SRC)
	$(CMD) \
		$(FLAGS) \
		--include_imports \
		--descriptor_set_out $@ \
		$^

clean:
	$(RM) $(PROTO_TARGET) $(MYPY_STUB_TARGET) $(PROTO_DESCRIPTOR)
