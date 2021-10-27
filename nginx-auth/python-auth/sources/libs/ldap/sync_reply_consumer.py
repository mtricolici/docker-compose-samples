import logging
import ldap
import ldapurl

from ldap.ldapobject import ReconnectLDAPObject
from ldap.syncrepl import SyncreplConsumer

from ..config import AppConfig

class LdapSyncReplyConsumer(ReconnectLDAPObject, SyncreplConsumer):

    def __init__(self, *args, **kwargs):
        ldap.ldapobject.ReconnectLDAPObject.__init__(self, *args, **kwargs)
        self._data = {}

    def syncrepl_get_cookie(self):
        logging.debug(">> syncrepl_get_cookie() invoked")
        if 'cookie' in self._data:
            logging.debug("cookie is '%s'", self._data['cookie'])
            return self._data['cookie']

    def syncrepl_set_cookie(self,cookie):
        logging.debug(">> syncrepl_set_cookie('%s') invoked", cookie)
        self._data['cookie'] = cookie
    
    def syncrepl_entry(self, dn, attributes, uuid):
        logging.debug(">> syncrepl_entry(dn = '%s')", dn)

    def syncrepl_delete(self,uuids):
        logging.debug(">> syncrepl_delete(..)")

    def syncrepl_refreshdone(self):
        logging.debug("Initial synchronization done.")


def start_sync_reply_consumer():
    ldap_url = "ldap://{}:{}".format(AppConfig.get['ldap']['host'], AppConfig.get['ldap']['port'])

    consumer = LdapSyncReplyConsumer(ldap_url)
    consumer.simple_bind_s(AppConfig.get['ldap']['user'], AppConfig.get['ldap']['password'])

    base_dn = AppConfig.get['ldap']['base_dn']
    ldap_search = consumer.syncrepl_search(base_dn, ldap.SCOPE_SUBTREE, 'refreshAndPersist',
        filterstr = '(|(objectClass=posixAccount)(objectClass=posixGroup))')

    while consumer.syncrepl_poll( all = 1, msgid = ldap_search):
        pass
