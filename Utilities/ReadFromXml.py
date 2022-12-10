import xml.etree.ElementTree as ET

from PMProj.Account import Account


def readFromXml():
    tree = ET.parse('in.xml')
    root = tree.getroot()
    data = list()
    for account in root:
        name = account[0].text
        website = account[1].text
        login = account[2].text
        password = account[3].text
        opt = dict()
        for optional in account[4]:
            opt.update({optional[0].text: optional[1].text})
        data.append(Account(name, website, [login], password, opt))
    return data
