from tkinter import *
from tkinter import font, messagebox

from PMProj.Account import Account


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
        self.listbox = Listbox(self.root, width=21, height=14, font=font.Font(family="Arial", size=20))
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
        self.account_data.clear()
        # current row number
        i = 1
        # current column number
        j = 1
        account_name_font = font.Font(family="Arial", size=20, weight='bold', underline=True)
        name = Label(text=account.name, font=account_name_font)
        name.grid(row=i, column=j, sticky='w')
        self.account_data.append(name)
        i = i + 1
        if account.extra_info:
            extra_info = Label(text='\t' + account.extra_info, font=font.Font(family="Arial", size=10, slant='italic'))
            extra_info.grid(row=i, column=j, sticky='w')
            self.account_data.append(extra_info)
        i = i + 1
        label_font = font.Font(family="Arial", size=11, weight='bold')
        account_data_font = font.Font(family="Arial", size=10)
        if account.website:
            website = Label(text='\tWebsite:', font=label_font)
            website.grid(row=i, column=j, sticky='w')
            self.account_data.append(website)
            website_data = Label(text='\t' + account.website, font=account_data_font)
            website_data.grid(row=i, column=j + 1, sticky='w')
            self.account_data.append(website_data)
            i = i + 2
        if account.login:
            login = Label(text='\tLogin:', font=label_font)
            login.grid(row=i, column=j, sticky='w')
            self.account_data.append(login)
            for l in account.login:
                login_data = Label(text='\t' + l, font=account_data_font)
                login_data.grid(row=i, column=j + 1, sticky='w')
                self.account_data.append(login_data)
                i = i + 1
            i = i + 1
        if account.password:
            password = Label(text='\tPassword:', font=label_font)
            password.grid(row=i, column=j, sticky='w')
            self.account_data.append(password)
            password_data = Label(text='\t' + account.password, font=account_data_font)
            password_data.grid(row=i, column=j + 1, sticky='w')
            self.account_data.append(password_data)
            i = i + 2
        for opt_key, opt_val in account.optional.items():
            optional = Label(text='\t' + opt_key + ':', font=label_font)
            optional.grid(row=i, column=j, sticky='w')
            self.account_data.append(optional)
            optional_data = Label(text='\t' + opt_val, font=account_data_font)
            optional_data.grid(row=i, column=j + 1, sticky='w')
            self.account_data.append(optional_data)
            i = i + 1
        edit_btn = Button(text='Edit', command=lambda: self.edit_account(account))
        edit_btn.grid(row=21, column=j + 3, sticky='e')
        self.account_data.append(edit_btn)
        remove_btn = Button(text='Remove', command=lambda: self.remove_account(account))
        remove_btn.grid(row=21, column=j + 4, sticky='e')
        self.account_data.append(remove_btn)

    def edit_account(self, account):
        for it in self.account_data:
            it.destroy()
        self.account_data.clear()
        # current row number
        i = 1
        # current column number
        j = 1
        account_name_font = font.Font(family="Arial", size=20, weight='bold', underline=False)
        name = Label(text='Account name: ', font=account_name_font)
        name.grid(row=i, column=j, sticky='w')
        self.account_data.append(name)
        name_entry = Entry(font=account_name_font)
        name_entry.insert(0, account.name)
        name_entry.grid(row=i, column=j + 1, sticky='w')
        self.account_data.append(name_entry)
        i = i + 1
        extra_info = Label(text='\t' + 'Extra info:', font=font.Font(family="Arial", size=10))
        extra_info.grid(row=i, column=j, sticky='w')
        self.account_data.append(extra_info)
        extra_info_entry = Entry(font=font.Font(family="Arial", size=10, slant='italic'))
        extra_info_entry.insert(0, account.extra_info if account.extra_info else '')
        extra_info_entry.grid(row=i, column=j + 1, sticky='w')
        self.account_data.append(extra_info_entry)
        i = i + 1

        label_font = font.Font(family="Arial", size=11, weight='bold')
        account_data_font = font.Font(family="Arial", size=10)
        website = Label(text='\tWebsite:', font=label_font)
        website.grid(row=i, column=j, sticky='w')
        self.account_data.append(website)
        website_entry = Entry(font=account_data_font)
        website_entry.insert(0, account.website if account.website else '')
        website_entry.grid(row=i, column=j + 1, sticky='w')
        self.account_data.append(website_entry)
        i = i + 2

        logins = []
        login = Label(text='\tLogin:', font=label_font)
        login.grid(row=i, column=j, sticky='w')
        logins.append(login)
        for index, l in enumerate(account.login):
            login_entry = Entry(font=account_data_font)
            login_entry.insert(0, l)
            login_entry.grid(row=i, column=j + 1, sticky='w')
            logins.append(login_entry)
            login_remove_btn = Button(text='Remove', command=lambda: self.remove_login((index + 1)*2))
            login_remove_btn.grid(row=i, column=j + 2, sticky='w')
            logins.append(login_remove_btn)
            i = i + 1
        login_add_new_btn = Button(text='Add new')
        login_add_new_btn.grid(row=i, column=j + 1, sticky='w')
        logins.append(login_add_new_btn)
        self.account_data.append(logins)
        i = i + 1

        password = Label(text='\tPassword:', font=label_font)
        password.grid(row=i, column=j, sticky='w')
        self.account_data.append(password)
        password_entry = Entry(font=account_data_font)
        password_entry.insert(0, account.password if account.password else '')
        password_entry.grid(row=i, column=j + 1, sticky='w')
        self.account_data.append(password_entry)
        i = i + 2

        optionals = []
        optional_info = []
        optional_label = Label(text='\tOptional fields:', font=label_font)
        optional_label.grid(row=i, column=j, sticky='w')
        i = i + 1
        optionals.append(optional_label)
        for opt_key, opt_val in account.optional.items():
            optional_key = Entry(font=label_font)
            optional_key.insert(0, opt_key)
            optional_key.grid(row=i, column=j, sticky='w')
            optional_data = Entry(font=label_font)
            optional_data.insert(0, opt_val)
            optional_data.grid(row=i, column=j + 1, sticky='w')
            optional_info.append((optional_key, optional_data))
            optional_remove_btn = Button(text='Remove')
            optional_remove_btn.grid(row=i, column=j + 2, sticky='w')
            optionals.append(optional_remove_btn)
            i = i + 1
        optional_add_new_btn = Button(text='Add new')
        optional_add_new_btn.grid(row=i, column=j + 1, sticky='w')
        optionals.append(optional_add_new_btn)
        self.account_data.append(optional_info)
        self.account_data.append(optionals)

    def remove_account(self, account):
        if messagebox.askyesno(message="Are you sure that you want to delete account?"):
            self.accounts_info.delete_account(account)
            self.listbox.delete(self.listbox.get(0, END).index(account.name))
            for it in self.account_data:
                it.destroy()
            self.account_data.clear()

    def remove_login(self, index):
        self.account_data[6][index - 1].destroy()
        self.account_data[6][index].destroy()
        del self.account_data[6][index]
        del self.account_data[6][index - 1]
        self.update_edited_window()

    def update_edited_window(self):
        name = self.account_data[1].get()
        extra_info = self.account_data[3].get()
        website = self.account_data[5].get()
        login = []
        for l in self.account_data[6][1:-1:2]:
            if l.get():
                login.append(l.get())
        password = self.account_data[8].get()
        optional = dict()
        for opt_key, opt_val in self.account_data[9]:
            if opt_key.get() and opt_val.get():
                optional.update({opt_key.get(): opt_val.get()})
        self.account_data += self.account_data[6]+[item for t in self.account_data[9] for item in t] + self.account_data[10]
        del self.account_data[10]
        del self.account_data[9]
        del self.account_data[6]
        self.edit_account(Account(name, extra_info, website, login, password, optional))
