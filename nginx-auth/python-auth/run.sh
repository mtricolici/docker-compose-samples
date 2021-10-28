#!/bin/bash

sdir="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

TAG=python-sample1


docker run -it --rm \
  --entrypoint /sources/main.py \
  -e APP_CONFIG_FILE=/application-config.yaml \
  -p 8081:8080 \
  -e LOG_LEVEL=DEBUG \
  -v $sdir/sources:/sources \
  -v $sdir/sample-config.yaml:/application-config.yaml \
  $TAG
