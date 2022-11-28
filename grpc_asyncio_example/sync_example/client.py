import logging

import grpc

from grpc_asyncio_example.protos import helloworld_pb2, helloworld_pb2_grpc


def client(target: str = "localhost:9999") -> None:
    with grpc.insecure_channel(target=target) as channel:
        stub: helloworld_pb2_grpc.GreeterStub = helloworld_pb2_grpc.GreeterStub(channel)
        response: helloworld_pb2.HelloReply = stub.SayHello(
            helloworld_pb2.HelloRequest(name="you"), timeout=10
        )
    logging.info("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    client()
