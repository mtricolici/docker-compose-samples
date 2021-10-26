
class LdapGroup:
    def __init__(self, dn, cn, group_id, members):
        self.dn = dn # Example: cn=admins,ou=groups,dc=zuzu,dc=com
        self.cn = cn # Example: admins
        self.group_id = group_id # example: 501
        self.members = members # Example: ['vasea1', 'vasea2', 'joric']

    def __repr__(self):
        return "LdapUser [dn={}, cn={}, group_id={}, members={}]".format(
                self.dn, self.cn, self.group_id, self.members)
