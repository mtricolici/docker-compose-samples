#!/bin/bash

TAG=python-sample1

docker build -t $TAG -f Dockerfile.debian .
