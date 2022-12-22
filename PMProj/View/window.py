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
        i = 1
        name = Label(text=f'\tName:\t\t{account.name}')
        name.grid(row=i, column=1, sticky='w')
        self.account_data.append(name)
        i = i + 1
        website = Label(text='\tWebsite:')
        website.grid(row=i, column=1, sticky='w')
        self.account_data.append(website)
        website_data = Label(text=account.website)
        website_data.grid(row=i, column=2, sticky='w')
        self.account_data.append(website_data)
        i = i + 1
        login = Label(text='\tLogin:')
        login.grid(row=i, column=1, sticky='w')
        self.account_data.append(login)
        for l in account.login:
            login_data = Label(text=l)
            login_data.grid(row=i, column=2, sticky='w')
            self.account_data.append(login_data)
            i = i + 1
        password = Label(text='\tPassword:')
        password.grid(row=i, column=1, sticky='w')
        self.account_data.append(password)
        password_data = Label(text=account.password)
        password_data.grid(row=i, column=2, sticky='w')
        self.account_data.append(password_data)
        i = i + 1
        for opt_key, opt_val in account.optional.items():
            optional = Label(text='\t'+opt_key)
            optional.grid(row=i, column=1, sticky='w')
            self.account_data.append(optional)
            optional_data = Label(text=opt_val)
            optional_data.grid(row=i, column=2, sticky='w')
            self.account_data.append(optional_data)
            i = i + 1
