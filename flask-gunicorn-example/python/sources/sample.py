#!/usr/bin/env python

from flask import Flask
from time import sleep

exemplu=Flask('why-this-string-is-needed-who-knows')
exemplu.config['DEBUG'] = True

@exemplu.route('/')
def index():
    sleep(0.5) # seconds.. simulate a slow backend ;)
    return "preved medved!"

