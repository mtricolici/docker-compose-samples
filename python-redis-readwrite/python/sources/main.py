#!/usr/bin/env python
import redis

redis_url = 'redis:6379'

r = redis.Redis(host='redis', port=6379, db=0)

print("writing to redis ...")
r.set('zuzu', '123')

print("reading from redis ...")
v = r.get('zuzu')
print("value is {}".format(v))
