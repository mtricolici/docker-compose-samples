#!/usr/bin/env python

from flask import Flask
from time import sleep
import random

app = Flask(__name__)

@app.route('/')
def index():
    sleep(random.uniform(0.02,0.5))
    return "preved"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
