#!/bin/bash

sdir="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

TAG=python-sample1


docker run -it --rm \
  -e APP_CONFIG_FILE=/application-config.yaml \
  -v $sdir/sources:/sources \
  -v $sdir/sample-config.yaml:/application-config.yaml \
  $TAG \
  /sources/main.py
