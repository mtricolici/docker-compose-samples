#!/usr/bin/env python

import logging
from libs.logger import AppLogger
from libs.config import AppConfig
from libs.ldap.data import LdapData
from libs.ldap.sync_reply_consumer import * #LdapSyncReplyConsumer

AppLogger.initialize()
AppConfig.load()

LdapData.fetch_data()
print(LdapData.users)

start_sync_reply_consumer()
