import enum
from tkinter import *
import tkinter as tk
from tkinter import messagebox

from PMProj.AccountsInfo import AccountsInfo


class Window:
    def __init__(self, accounts_info):
        self.root = Tk()
        self.root.columnconfigure(2, {f'minsize': 475})
        self.root.geometry("950x550")#("%dx%d" % (self.root.winfo_screenwidth()/2, self.root.winfo_screenheight()/2))
        self.accounts_info=accounts_info
        self.name = Label(text="Name:")
        self.name.grid(row=1, column=2, sticky = 'w')
        self.website = Label(text="Website:")
        self.website.grid(row=2, column=2, sticky = 'w')
        self.login = Label(text="Login:")
        self.login.grid(row=3, column=2, sticky = 'w')
        self.password = Label(text="Password:")
        self.password.grid(row=4, column=2, sticky = 'w')

        self.listbox = Listbox(self.root, width= 70,
                               height=30)

        get_account_info =Button(text="get_account_info", command=self.get_account_info)
        get_account_info.grid(row=2, column=1, padx=10, pady=20)
        for values in self.accounts_info.accounts_list:
            self.listbox.insert(END, values.name)
        self.listbox.grid(column=1, row=1, rowspan=15)
        #self.listbox.bind('<Double-1>', update('s'))
        self.root.mainloop()

    def get_account_info(self):
        sel = self.listbox.curselection()
        string = self.listbox.get(sel[0])
        account = self.accounts_info.find_account(string)
        self.update(account)

    def update(self, account):
        #account = self.accounts_info.find_account(name)
        self.name['text'] = f'\tName:\t\t{account.name}'
        self.website['text'] = f'\tWebsite:\t\t{account.website}'
        self.login['text'] = f'\tLogin:\t\t{account.login}'
        self.password['text'] = f'\tPassword:\t{account.password}'
        self.root.mainloop()
        print(self.root.winfo_reqwidth())
        print(self.root.winfo_reqheight())

        #def load_accounts(self, accounts_info)

