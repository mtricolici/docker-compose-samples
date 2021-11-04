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
#print(LdapData.get_users_groups_dictionary())

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
        token = auth_header[len("Bearer"):].strip()
        logging.debug("auth. verify token: %s", token)
        helper = JWTHelper()
        token = helper.verify(token)
        logging.debug("token: %s", token)

        ldapUserGroups = LdapData.get_users_groups_dictionary()

        user_id = token['user']
        if user_id not in ldapUserGroups:
            raise ValueError("User not found in LDAP. removed?")

        #This header is always present! nginx sets it
        requested_uri = request.headers['X-Original-URI']

        #POC: just a POC of 'authorization!'
        if requested_uri.startswith("/admin/"):
            if "admins" not in ldapUserGroups[user_id]: # check user groups
                raise ValueError("User is not admin. Access denied!")

        logging.debug("user '%s' is ok to go ;)")
        return Response("ok;)", status=200, mimetype="text/plain")
    except Exception as e:
        logging.error(e)
        return Response("Access denied", status=401, mimetype="text/plain")

@app.route('/generate-token.exe', methods = ['POST'])
def generate_token():
    try:
        user = request.form['user']
        logging.debug("/generate-token.exe for '%s'", user)
        ldapUserGroups = LdapData.get_users_groups_dictionary()

        if user not in ldapUserGroups:
            raise ValueError("User not found in LDAP")
        email = "{}@zuzu.com".format(user) #TODO: read email from ldap
        helper = JWTHelper()
        token, refresh_token = helper.generate(user, email)
        return """Prevet '{}'!
Please find your token: {}\n\n

Usage example:
curl -H "Authorization: Bearer {}" http://localhost:8888/admin/\n\n

Your refresh token is: {}

""".format(user, token, token, refresh_token)

        
    except Exception as e:
        logging.error(e)
        return "Error. I cannot generate a token for you. I'm very very sorry"

