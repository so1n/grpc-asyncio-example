import gevent.monkey

gevent.monkey.patch_all()
import gevent

gevent.hub.get_hub()

import grpc.experimental.gevent

grpc.experimental.gevent.init_gevent()
from grpc_asyncio_example.sync_example.server import serve

if __name__ == "__main__":
    import logging

    logging.basicConfig()
    serve().wait_for_termination()
