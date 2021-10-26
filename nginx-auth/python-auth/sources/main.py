#!/usr/bin/env python

from libs.ldap import LdapHelper

ldap_host = '192.168.100.24'
ldap_port = 1389
ldap_user = 'cn=admin,dc=zuzu,dc=com'
ldap_password = '123'
ldap_users_dn = 'ou=users,dc=zuzu,dc=com'
ldap_groups_dn = 'ou=groups,dc=zuzu,dc=com'

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
