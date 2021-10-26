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

    def _decode(self, value):
        if isinstance(value, bytes):
            return value.decode('utf-8')
        return value

    def fetch_users(self, baseDn):
        searchResult = self.__ldap.search_s(baseDn, ldap.SCOPE_ONELEVEL,
                '(objectClass=inetOrgPerson)')
        users=[]
        for obj in searchResult:
            users.append(LdapUser(
                    dn       = self._decode(obj[0]),
                    cn       = self._decode(obj[1]['cn'][0]),
                    user_id  = self._decode(obj[1]['uidNumber'][0]),
                    group_id = self._decode(obj[1]['gidNumber'][0]),
                    mail     = self._decode(obj[1]['mail'][0])))
        return users
