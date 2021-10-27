#!/usr/bin/env python

import logging
from libs.logger import AppLogger
from libs.config import AppConfig
from libs.ldap import LdapHelper

AppLogger.initialize()
AppConfig.load()

ldap_host = AppConfig.get['ldap']['host']
ldap_port = AppConfig.get['ldap']['port']
ldap_user = AppConfig.get['ldap']['user']
ldap_password = AppConfig.get['ldap']['password']
ldap_users_dn = AppConfig.get['ldap']['users_dn']
ldap_groups_dn = AppConfig.get['ldap']['groups_dn']

ldap=LdapHelper(ldap_host, ldap_port, ldap_users_dn, ldap_groups_dn)

if (ldap.connect(ldap_user, ldap_password)):
    logging.debug("LDAP users:")
    res = ldap.fetch_users()
    for obj in res:
        logging.debug(obj)

    logging.debug("LDAP groups:")
    res = ldap.fetch_groups()
    for obj in res:
        logging.debug(obj)
