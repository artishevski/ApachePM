from PMProj.AccountsInfo import AccountsInfo
from PMProj.View.window import Window

if __name__ == "__main__":
    data = AccountsInfo()
    window = Window(data)
    #window.update(data[0])
    #for i in data:
    #    i.get_info()
    #    print()

