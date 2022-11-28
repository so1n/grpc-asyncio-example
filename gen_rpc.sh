#!/bin/bash
target_p='grpc_asyncio_example'
source_p='protos'
rm -r "${target_p:?}/${source_p:?}"*

poetry run python -m grpc_tools.protoc \
  --mypy_grpc_out=./ \
  --mypy_out=./ \
  --python_out=./ \
  --grpc_python_out=./ \
  -I protos $(find ./protos -name '*.proto')

poetry run python -m grpc_tools.protoc \
  -I protos $(find ./protos -name '*.proto') \
  --python_betterproto_out=./${target_p:?}/${source_p:?}
