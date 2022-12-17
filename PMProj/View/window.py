from tkinter import *


class Window:
    def __init__(self, accounts_info):
        self.root = Tk()
        self.root.title('BulbaPM')
        # self.root.rowconfigure(0, pad=1)
        # self.root.rowconfigure(1, pad=1)
        self.root.columnconfigure(0, pad=20)
        self.root.columnconfigure(1)
        self.root.geometry("950x550")
        self.account_data = []
        self.accounts_info = accounts_info
        self.search = Entry(width=40)
        self.search.grid(column=0, row=0)

        self.listbox = Listbox(self.root, width=40, height=30)
        self.listbox.grid(column=0, row=1, rowspan=20)

        get_account_info = Button(text="get_account_info", command=self.get_account_info, height=2, width=33)
        get_account_info.grid(row=21, column=0)
        for values in self.accounts_info.accounts_list:
            self.listbox.insert(END, values.name)

        self.root.mainloop()

    def get_account_info(self):
        sel = self.listbox.curselection()
        string = self.listbox.get(sel[0])
        account = self.accounts_info.find_account(string)
        self.update(account)

    def update(self, account):
        for it in self.account_data:
            it.destroy()
        name = Label(text=f'\tName:\t\t{account.name}')
        website = Label(text=f'\tWebsite:\t\t{account.website}')
        login = Label(text=f'\tLogin:\t\t{account.login}')
        password = Label(text=f'\tPassword:\t{account.password}')
        self.account_data = [name, website, login, password]

        name.grid(row=1, column=1, sticky='w')
        website.grid(row=2, column=1, sticky='w')
        login.grid(row=3, column=1, sticky='w')
        password.grid(row=4, column=1, sticky='w')
