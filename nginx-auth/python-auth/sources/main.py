#!/usr/bin/env python

import re
import logging
from flask import Flask
from flask import Response
from flask import request


# Why this is needed? I don't know :D It works without it too
import gevent.monkey
gevent.monkey.patch_all()

from libs.logger import AppLogger
from libs.config import AppConfig
from libs.ldap.data import LdapData
from libs.jwt_helper import JWTHelper

AppLogger.initialize()
AppConfig.load()

LdapData.fetch_data()
#print(LdapData.users)

app=Flask(__name__)
app.config['DEBUG'] = True # Does this work with gunicorn?
app.config['WORKERS'] = 3 # TODO: this does not work. whyyyyyyyyyyy

@app.route('/auth')
def handle_auth():
    try:
        if 'Authorization' not in request.headers:
            raise ValueError("Authorization header is missing")
        auth_header = request.headers['Authorization'].strip()
        if not re.match("^Bearer", auth_header):
            raise ValueError("Unsupporte authentication method")
        token = auth_header.removeprefix("Bearer").strip()
        logging.debug("auth. verify token: %s", token)
        helper = JWTHelper()
        token = helper.verify(token)
        logging.debug("token: %s", token)

        user_id = token['user']
        if user_id not in LdapData.users:
            raise ValueError("User not found in LDAP. removed?")

        #This header is always present! nginx sets it
        requested_uri = request.headers['X-Original-URI']

        #POC: just a POC of 'authorization!'
        if requested_uri.startswith("/admin/"):
            if "admins" not in LdapData.users[user_id]: # check user groups
                raise ValueError("User is not admin. Access denied!")
        logging.debug("user '%s' is ok to go ;)")
        return Response("ok;)", status=200, mimetype="text/plain")
    except Exception as e:
        logging.error(e)
        return Response("Access denied", status=401, mimetype="text/plain")

@app.route('/generate-token.exe', methods = ['POST'])
def generate_token():
    user = request.form['user'] #TODO: validate this is present
    logging.debug("/generate-token.exe for '%s'", user)
    email = "{}@zuzu.com".format(user) #TODO: read email from ldap
    #TODO: verify presence of the user ;)
    helper = JWTHelper()
    token = helper.generate(user, email)
    if token is None:
        return "Unknown error:( Try again later"

    return """Prevet '{}'!
Please find your token: {}

Usage example:
curl -H "Authorization: Bearer {}" http://localhost:8888/admin/""".format(user, token, token)
