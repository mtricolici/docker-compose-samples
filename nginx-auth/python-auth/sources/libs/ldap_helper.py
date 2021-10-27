import ldap
import logging

from .ldap_user import LdapUser
from .ldap_group import LdapGroup

class LdapHelper:

    def __init__(self, host, port, users_dn, groups_dn):
        self.__ldap_host = host
        self.__ldap_port = port
        self.__users_dn  = users_dn
        self.__groups_dn = groups_dn

    def connect(self, user, password):
        try:
            self.__ldap = ldap.initialize('ldap://{0}:{1}'.format(
                self.__ldap_host, self.__ldap_port))
            self.__ldap.simple_bind_s(user, password)
            return True
        except ldap.INVALID_CREDENTIALS:
            logging.error("invalid ldap credentials")
            return False
        except ldap.SERVER_DOWN:
            logging.error("LDAP server is not reachable")
            return False

    def _decode(self, value):
        if isinstance(value, bytes):
            return value.decode('utf-8')
        if isinstance(value, list):
            res=[]
            for item in value:
                res.append(self._decode(item))
            return res
        return value

    def fetch_users(self):
        search_result = self.__ldap.search_s(self.__users_dn, ldap.SCOPE_ONELEVEL,
            '(objectClass=inetOrgPerson)')
        users=[]
        for obj in search_result:
            users.append(LdapUser(
                dn       = self._decode(obj[0]),
                cn       = self._decode(obj[1]['cn'][0]),
                user_id  = self._decode(obj[1]['uidNumber'][0]),
                group_id = self._decode(obj[1]['gidNumber'][0]),
                mail     = self._decode(obj[1]['mail'][0])))
        return users

    def fetch_groups(self):
        search_result = self.__ldap.search_s(self.__groups_dn, ldap.SCOPE_ONELEVEL,
                '(objectClass=posixGroup)')
        groups=[]
        for g in search_result:
            groups.append(LdapGroup(
                dn       = self._decode(g[0]),
                cn       = self._decode(g[1]['cn'][0]),
                group_id = self._decode(g[1]['gidNumber'][0]),
                members  = self._decode(g[1]['memberUid'])))
        return groups
