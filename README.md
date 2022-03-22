# Grpc Envoy Example

## Objectives

* Set up python environment

## Installation

```bash

docker-compose up --build -d --scale storage_server=4

python3 client.py

./rest_client.sh
```

### Clone Submodule
```
git submodule update --init
```

## TODO

- [x] Transcode gRPC to REST
- [ ] CI/CD
- [ ] Unit test
- [ ] ORM
- [ ] ~~Swagger integration~~ -> Will be integrated into CI/CD
