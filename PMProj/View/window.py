from tkinter import *
from tkinter import font


class Window:
    def __init__(self, accounts_info):
        self.root = Tk()
        self.root.title('BulbaPM')
        # self.root.rowconfigure(0, pad=1)
        # self.root.rowconfigure(1, pad=1)
        self.root.columnconfigure(0, pad=20)
        self.root.columnconfigure(1)
        self.root.geometry("950x545")
        self.account_data = []
        self.accounts_info = accounts_info
        self.search = Entry(width=35, font=font.Font(family="Arial", slant='italic', size=12))
        self.search.grid(column=0, row=0)
        self.listbox = Listbox(self.root, width=21, height=14,font=font.Font(family="Arial", size=20))
        self.listbox.grid(column=0, row=1, rowspan=20)
        get_account_info = Button(text="get_account_info", command=self.get_account_info, height=1, width=19,
                                  font=font.Font(family="Arial", size=20))
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
        #current row nummber
        i = 1
        account_name_font= font.Font(family= "Arial", size=20, weight='bold', underline=True)
        name = Label(text=account.name, font=account_name_font)
        name.grid(row=i, column=1, sticky='w')
        self.account_data.append(name)
        i = i + 1
        if account.extra_info is not None:
            extra_info = Label(text='\t'+account.extra_info, font=font.Font(family= "Arial", size=10, slant='italic'))
            extra_info.grid(row=i, column=1, sticky='w')
            self.account_data.append(extra_info)
        i=i+1
        label_font = font.Font(family= "Arial", size=11, weight='bold')
        website = Label(text='\tWebsite:', font=label_font)
        website.grid(row=i, column=1, sticky='w')
        self.account_data.append(website)
        account_data_font = font.Font(family= "Arial", size=10)
        website_data = Label(text='\t'+account.website, font=account_data_font)
        website_data.grid(row=i, column=2, sticky='w')
        self.account_data.append(website_data)
        i = i + 2
        login = Label(text='\tLogin:', font=label_font)
        login.grid(row=i, column=1, sticky='w')
        self.account_data.append(login)
        for l in account.login:
            login_data = Label(text='\t'+l, font=account_data_font)
            login_data.grid(row=i, column=2, sticky='w')
            self.account_data.append(login_data)
            i = i + 1
        i = i + 1
        password = Label(text='\tPassword:', font=label_font)
        password.grid(row=i, column=1, sticky='w')
        self.account_data.append(password)
        password_data = Label(text='\t'+account.password, font=account_data_font)
        password_data.grid(row=i, column=2, sticky='w')
        self.account_data.append(password_data)
        i = i + 2
        for opt_key, opt_val in account.optional.items():
            optional = Label(text='\t'+opt_key+':', font=label_font)
            optional.grid(row=i, column=1, sticky='w')
            self.account_data.append(optional)
            optional_data = Label(text='\t'+opt_val, font=account_data_font)
            optional_data.grid(row=i, column=2, sticky='w')
            self.account_data.append(optional_data)
            i = i + 1
