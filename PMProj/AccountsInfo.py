from Utilities.ReadFromXml import readFromXml

class AccountsInfo:
    def __init__(self):
        self.accounts_list = readFromXml()

    def delete_account(self, account):
        self.accounts_list.remove(account)

    def find_account(self, name):
        for acc in self.accounts_list:
            if acc.name == name:
                return acc
        return ''