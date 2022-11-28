import asyncio
import logging

from grpclib.client import Channel

from grpc_asyncio_example.protos import helloworld


async def client() -> None:
    channel: Channel = Channel(host="localhost", port=9999)
    response: helloworld.HelloReply = await helloworld.GreeterStub(channel).say_hello(
        hello_request=helloworld.HelloRequest(name="you")
    )
    logging.info(response)

    # don't forget to close the channel when done!
    channel.close()


if __name__ == "__main__":
    asyncio.run(client())
