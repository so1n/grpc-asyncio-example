from grpc_asyncio_example.betterproto_example.server import serve

if __name__ == "__main__":
    import asyncio

    import uvloop

    uvloop.install()

    async def main() -> None:
        await (await serve()).wait_closed()

    asyncio.run(main())
