import os

from Encryption.ViginereExtended import ViginereExtended
from PMProj.Account import Account
import xml.etree.ElementTree as ET


class AccountsInfo:
    def __init__(self, e1, e2):
        self.accounts_dict = dict()
        self.encrypt_code = e1 if e1 else '0'
        self.decrypt_code = e2 if e2 else '0'

    def delete_account(self, id):
        del self.accounts_dict[id]

    def find_account(self, name):
        for acc in self.accounts_dict.values():
            if acc.name == name:
                return acc
        return ''

    def update_account(self, account):
        self.accounts_dict.update({account.id: account})

    def is_name_available(self, name, id):
        for acc in self.accounts_dict.values():
            if acc.name.lower() == name.lower() and acc.id != id:
                return False
        return True

    def add_account(self):
        for i in range(1000):
            if not self.accounts_dict.__contains__(i):
                account = Account(i)
                self.accounts_dict.update({i: account})
                return account

    def readFromXml(self):
        decoder = ViginereExtended(self.encrypt_code)
        if not os.path.isfile('in.xml'):
            return dict()
        tree = ET.parse('in.xml')
        root = tree.getroot()
        for ind, account in enumerate(root):
            login = []
            opt = dict()
            name = website = password = extra_info = None
            for account_info in account:
                if account_info.tag == 'name':
                    name = decoder.decode(account_info.text)
                elif account_info.tag == 'extra_info':
                    extra_info = decoder.decode(account_info.text)
                elif account_info.tag == 'website':
                    website = decoder.decode(account_info.text)
                elif account_info.tag == 'login':
                    login.append(decoder.decode(account_info.text))
                elif account_info.tag == 'password':
                    password = decoder.decode(account_info.text)
                else:
                    opt.update({decoder.decode(account_info.tag.replace('_', ' ')): decoder.decode(account_info.text)})
            if name:
                self.accounts_dict.update({ind + 1: Account(ind + 1, name, extra_info, website, login, password, opt)})

    def writeToXml(self):
        encoder = ViginereExtended(self.decrypt_code)
        data=ET.Element('data')
        for acc in self.accounts_dict.values():
            account = ET.SubElement(data, 'account')
            if acc.name:
                name = ET.SubElement(account, 'name')
                name.text = encoder.encode(acc.name)
            if acc.extra_info:
                extra_info = ET.SubElement(account, 'extra_info')
                extra_info.text = encoder.encode(acc.extra_info)
            if acc.website:
                website = ET.SubElement(account, 'website')
                website.text = encoder.encode(acc.website)
            for l in acc.login:
                login = ET.SubElement(account, 'login')
                login.text = encoder.encode(l)
            if acc.password:
                password = ET.SubElement(account, 'password')
                password.text = encoder.encode(acc.password)
            for key, val in acc.optional.items():
                opt_key = ET.SubElement(account, encoder.encode(key.replace(' ', '_')))
                opt_key.text = encoder.encode(val)
        ET.ElementTree(data).write("in.xml")
