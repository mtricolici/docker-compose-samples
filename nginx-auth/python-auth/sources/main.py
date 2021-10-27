#!/usr/bin/env python

from libs.config import AppConfig
from libs.ldap import LdapHelper

AppConfig.load()

ldap_host = AppConfig.get['ldap']['host']
ldap_port = AppConfig.get['ldap']['port']
ldap_user = AppConfig.get['ldap']['user']
ldap_password = AppConfig.get['ldap']['password']
ldap_users_dn = AppConfig.get['ldap']['users_dn']
ldap_groups_dn = AppConfig.get['ldap']['groups_dn']

ldap=LdapHelper(ldap_host, ldap_port, ldap_users_dn, ldap_groups_dn)

if (ldap.connect(ldap_user, ldap_password)):
    print("LDAP users:")
    res = ldap.fetch_users()
    for obj in res:
        print(obj)

    print("LDAP groups:")
    res = ldap.fetch_groups()
    for obj in res:
        print(obj)
