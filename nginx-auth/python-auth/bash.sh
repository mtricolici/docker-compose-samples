#!/bin/bash

sdir="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

TAG=python-sample1


docker run -it --rm \
  -v $sdir/sources:/sources \
  $TAG \
  bash
