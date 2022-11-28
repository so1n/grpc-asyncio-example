import asyncio
import logging

import grpc

from grpc_asyncio_example.protos import helloworld_pb2, helloworld_pb2_grpc


async def client(target: str = "localhost:9999") -> None:
    async with grpc.aio.insecure_channel(target) as channel:
        stub: helloworld_pb2_grpc.GreeterStub = helloworld_pb2_grpc.GreeterStub(channel)
        response: helloworld_pb2.HelloRequest = await stub.SayHello(
            helloworld_pb2.HelloRequest(name="you")
        )
    logging.info("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(client())
