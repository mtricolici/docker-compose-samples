import logging
from datetime import datetime

from .reader import LdapReader
from ..config import AppConfig

class LdapData:
    __last_fetch = None
    __data = {}
    # Structure: userid as KEY and user groups string list as VALUE
    # Example of an entry in this dictionary
    # 'user1' => ['developers', 'group2', 'group3']

    def get_users_groups_dictionary():
        #TODO: check if _last_fetch is too old and invoke a 'refresh'... async?
        return LdapData.__data

    def fetch_data():
        ldap = LdapReader(
            AppConfig.get['ldap']['host'],
            AppConfig.get['ldap']['port'],
            AppConfig.get['ldap']['users_dn'],
            AppConfig.get['ldap']['groups_dn'])

        if(not ldap.connect(AppConfig.get['ldap']['user'], AppConfig.get['ldap']['password'])):
            logging.error("could not connect to ldap")
            return

        users = ldap.fetch_users()
        groups = ldap.fetch_groups()

        new_data = {}
        for u in users:
            new_data[u.cn] = []
            for g in groups:
                if u.cn in g.members:
                    new_data[u.cn].append(g.cn)
        
        LdapData.__last_fetch = datetime.now()
        LdapData.__data = new_data
