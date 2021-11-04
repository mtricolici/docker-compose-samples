#!/bin/bash

sdir="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

TAG=python-sample1

docker run -it --rm \
  -e APP_CONFIG_FILE=/application-config.yaml \
  -p 8081:8080 \
  -e LOG_LEVEL=DEBUG \
  -v $sdir/sources:/app \
  -v $sdir/sample-config.yaml:/application-config.yaml \
  --tmpfs /my-tmp-dir \
  --name debug_python_sample1 \
  $TAG
