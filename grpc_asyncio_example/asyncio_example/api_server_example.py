from typing import Any

import grpc
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse

from grpc_asyncio_example.protos import helloworld_pb2, helloworld_pb2_grpc


async def helloword(request: Request) -> JSONResponse:
    stub: helloworld_pb2_grpc.GreeterStub = helloworld_pb2_grpc.GreeterStub(
        request.app.state.channel
    )
    response: helloworld_pb2.HelloRequest = await stub.SayHello(
        helloworld_pb2.HelloRequest(name="you")
    )
    return JSONResponse({"name": response.name})


def create_app() -> Starlette:
    app: Starlette = Starlette()

    async def _before_server_start(*_: Any) -> None:
        app.state.channel = grpc.aio.insecure_channel("localhost:9999")

    async def _after_server_stop(*_: Any) -> None:
        await app.state.channel.close()

    app.add_event_handler("startup", _before_server_start)
    app.add_event_handler("shutdown", _after_server_stop)
    return app


if __name__ == "__main__":

    import uvicorn  # type: ignore

    starlette_app: Starlette = create_app()
    uvicorn.run(starlette_app)
