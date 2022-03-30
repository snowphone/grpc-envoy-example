FROM python:3.10

COPY ./requirements.txt requirements.txt
COPY ./server.py server.py
COPY ./storage_pb2.py storage_pb2.py
COPY ./storage_pb2_grpc.py storage_pb2_grpc.py
COPY ./time_pb2.py time_pb2.py
copy ./time_pb2_grpc.py time_pb2_grpc.py

RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "server.py"]
