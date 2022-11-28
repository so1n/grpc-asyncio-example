from .client import client
from .server import serve


async def main() -> None:
    server = await serve()
    asyncio.create_task(server.wait_for_termination())
    await client()
    await server.stop(1)


if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(
        format="[%(asctime)s %(levelname)s] %(message)s",
        datefmt="%y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    asyncio.run(main())
