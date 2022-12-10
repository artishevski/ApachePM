from PMProj.AccountsInfo import AccountsInfo
from PMProj.View.window import Window
from Utilities.ReadFromXml import readFromXml

if __name__ == "__main__":
    data = AccountsInfo()
    window = Window(data)
    #window.update(data[0])
    #for i in data:
    #    i.get_info()
    #    print()

