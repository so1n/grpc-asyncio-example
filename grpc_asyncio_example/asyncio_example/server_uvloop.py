import asyncio
import logging

from grpc_asyncio_example.asyncio_example.server import serve

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    import uvloop

    uvloop.install()

    async def main() -> None:
        await (await serve()).wait_for_termination()

    asyncio.run(main())
