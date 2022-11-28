import asyncio

from grpclib.server import Server

from grpc_asyncio_example.protos import helloworld


class HelloWorldService(helloworld.GreeterBase):
    async def say_hello(
        self, request: "helloworld.HelloRequest"
    ) -> "helloworld.HelloReply":
        await asyncio.sleep(request.sleep_millisecond / 1000)
        return helloworld.HelloReply(message="Hello, %s!" % request.name)


async def serve() -> Server:
    server: Server = Server([HelloWorldService()])
    await server.start("localhost", 9999)
    return server


if __name__ == "__main__":

    async def main() -> None:
        await (await serve()).wait_closed()

    asyncio.run(main())
