from .client import client
from .server import serve

if __name__ == "__main__":
    import logging

    logging.basicConfig(
        format="[%(asctime)s %(levelname)s] %(message)s",
        datefmt="%y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    serve()
    client()
