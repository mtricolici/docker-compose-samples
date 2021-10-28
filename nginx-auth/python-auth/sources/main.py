#!/usr/bin/env python

import logging
from libs.logger import AppLogger
from libs.config import AppConfig
from libs.ldap.data import LdapData

AppLogger.initialize()
AppConfig.load()

LdapData.fetch_data()
print(LdapData.users)
