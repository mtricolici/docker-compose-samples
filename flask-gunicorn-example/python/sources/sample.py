#!/usr/bin/env python

from flask import Flask
from time import sleep
import requests

import gevent.monkey
gevent.monkey.patch_all()


exemplu=Flask('why-this-string-is-needed-who-knows')
exemplu.config['DEBUG'] = True

@exemplu.route('/')
def index():
    r = requests.get("http://slow-backend:8080/")
    return "response-code:{}, text:{}".format(r.status_code, r.text)

