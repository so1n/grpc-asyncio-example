import asyncio
import logging

import grpc

from grpc_asyncio_example.protos import helloworld_pb2, helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    async def SayHello(
        self, request: helloworld_pb2.HelloRequest, context: grpc.aio.ServicerContext
    ) -> helloworld_pb2.HelloReply:
        await asyncio.sleep(request.sleep_millisecond / 1000)
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)


async def serve(target: str = "localhost:9999") -> grpc.aio.Server:
    server: grpc.aio.Server = grpc.aio.server()
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(target)
    logging.info("Starting server on %s", target)
    await server.start()
    return server


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    async def main() -> None:
        await (await serve()).wait_for_termination()

    asyncio.run(main())
