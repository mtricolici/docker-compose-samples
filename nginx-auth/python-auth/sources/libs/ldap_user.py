
class LdapUser:
    def __init__(self, dn, cn, user_id, group_id, mail):
        self.dn = dn
        self.cn = cn
        self.user_id = user_id
        self.group_id = group_id
        self.mail = mail

    def __repr__(self):
        return "LdapUser [dn={}, cn={}, user_id={}, group_id={}, mail={}]".format(
                self.dn, self.cn, self.user_id, self.group_id, self.mail)
