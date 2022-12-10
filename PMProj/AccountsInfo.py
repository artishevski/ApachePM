from Utilities.ReadFromXml import readFromXml

class AccountsInfo:
    def __init__(self):
        self.accounts_list = readFromXml()

    def find_account(self, name):
        for acc in self.accounts_list:
            if acc.name == name:
                return acc
        return ''