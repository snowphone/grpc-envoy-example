# Grpc Envoy Example

## Objectives

* Set up python environment

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 server.py &

python3 client.py
```

### Clone Submodule
```
git submodule update --init
```

## Transcoding Example
```
curl -i -X POST http://localhost/v1/storage?key=hello&value=world

curl -i http://localhost/v1/storage/hello

curl -i http://localhost/v1/storage/expect_not_exist
```

## TODO

- [x] Transcode gRPC to REST
- [ ] CI/CD
- [ ] Unit test
- [ ] ORM
- [ ] Swagger integration
