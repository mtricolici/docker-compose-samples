#!/usr/bin/env python

from flask import Flask

exemplu=Flask('why-this-string-is-needed-who-knows')
exemplu.config['DEBUG'] = True

@exemplu.route('/')
def index():
    return "preved medved!"

