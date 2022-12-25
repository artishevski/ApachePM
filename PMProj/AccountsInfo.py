from PMProj.Account import Account
from Utilities.ReadFromXml import readFromXml


class AccountsInfo:
    def __init__(self):
        self.accounts_dict = readFromXml()

    def delete_account(self, id):
        del self.accounts_dict[id]

    def find_account(self, name):
        for acc in self.accounts_dict.values():
            if acc.name == name:
                return acc
        return ''

    def update_account(self, account):
        self.accounts_dict.update({account.id: account})

    def add_account(self):
        for i in range(1000):
            if not self.accounts_dict.__contains__(i):
                account = Account(i)
                self.accounts_dict.update({i: account})
                return account
