#!/usr/bin/env python

import logging
import signal

from libs.logger import AppLogger
from libs.config import AppConfig
from libs.ldap.data import LdapData
from libs.ldap.sync import *

def shutdown(signum, frame):
    logging.info("!!!signal handler '%s'", signum)
    stop_synchronization_job()
    exit(0)

signal.signal(signal.SIGINT, shutdown) # handle ctrl+c

AppLogger.initialize()
AppConfig.load()

LdapData.fetch_data()
print(LdapData.users)

start_ldap_synchronization_job()

input("")
