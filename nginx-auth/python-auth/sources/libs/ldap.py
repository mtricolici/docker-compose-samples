import ldap

from .ldap_user import LdapUser

class LdapHelper:

    def __init__(self, host, port):
        self.__ldap_host = host
        self.__ldap_port = port

    def connect(self, user, password):
        try:
            self.__ldap = ldap.initialize('ldap://{0}:{1}'.format(
                self.__ldap_host, self.__ldap_port))
            self.__ldap.simple_bind_s(user, password)
            return True
        except ldap.INVALID_CREDENTIALS:
            print("Error: invalid credentials")
            return False

    def fetch_users(self, baseDn):
        searchResult = self.__ldap.search_s(baseDn, ldap.SCOPE_ONELEVEL,
                '(objectClass=inetOrgPerson)')
        users=[]
        for obj in searchResult:
            users.append(LdapUser(
                    dn=obj[0],
                    cn='ceva',
                    user_id='ceva',
                    group_id='ceva',
                    mail='ceva'))
        return users
#user.dn = obj[0]
#user.cn=obj[1]['cn'][0]
#print(type(obj[1]['cn'][0]))
#exit(0)
#user.groupId=obj[1]['gidNumber'][0]
#print(obj)
