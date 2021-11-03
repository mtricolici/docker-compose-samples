#!/bin/sh

# Number of requests to perform
NRP=5000

# Number of multiple requests to make at a time
NMCR=200

ab -r -n $NRP -c $NMCR  http://localhost:8080/
