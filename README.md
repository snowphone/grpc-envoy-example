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

### Clone submodule
```
git submodule update --init
```

## TODO

- [ ] Transcode gRPC to REST
- [ ] CI/CD
- [ ] Unit test
- [ ] ORM
