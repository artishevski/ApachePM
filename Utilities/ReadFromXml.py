import xml.etree.ElementTree as ET

from PMProj.Account import Account


def readFromXml():
    tree = ET.parse('in.xml')
    root = tree.getroot()
    data = list()
    for account in root:
        login = []
        opt = dict()
        for account_info in account:
            if account_info.tag == 'name':
                name = account_info.text
            elif account_info.tag == 'website':
                website = account_info.text
            elif account_info.tag == 'login':
                login.append(account_info.text)
            elif account_info.tag == 'password':
                password = account_info.text
            else:
                opt.update({account_info.tag: account_info.text})
        data.append(Account(name, website, login, password, opt))
    return data
