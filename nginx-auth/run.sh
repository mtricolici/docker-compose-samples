#!/bin/bash
set -e

echo "remove all stopped containers ..."
docker container prune -f

echo "stop & remove all running containers ..."
docker ps -q|xargs -I{} docker rm -f {}

echo "remove all volumes ..."
docker volume ls -q|xargs -I{} docker volume rm {}


docker-compose up
