import ldap

class LdapHelper:
  def zuzu1(self):
    l = ldap.initialize('ldap://192.168.100.24:1389')
    res = l.search_s('ou=users,dc=zuzu,dc=com', ldap.SCOPE_ONELEVEL)
    print(res)
    print("zuzu1")
