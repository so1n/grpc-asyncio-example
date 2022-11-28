from .client import client
from .server import serve


async def main() -> None:
    await serve()
    await client()


if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(
        format="[%(asctime)s %(levelname)s] %(message)s",
        datefmt="%y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    asyncio.run(main())
