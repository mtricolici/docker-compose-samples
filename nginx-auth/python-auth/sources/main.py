#!/usr/bin/env python

from libs.ldap import LdapHelper

ldap=LdapHelper('192.168.100.24', 1389)

if (ldap.connect('cn=admin,dc=zuzu,dc=com', '123')):
  res = ldap.fetch_users('ou=users,dc=zuzu,dc=com')
  print("\n\n")
  print(res)

print("end")
