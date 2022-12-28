from functools import partial
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
        self.var = StringVar()
        self.var.trace("w", self.search_account)
        self.search = Entry(width=35, font=font.Font(family="Arial", slant='italic', size=12), textvariable=self.var)
        self.search.grid(column=0, row=0)
        self.listbox = Listbox(self.root, width=21, height=14, font=font.Font(family="Arial", size=20))
        self.listbox.bind("<<ListboxSelect>>", self.get_account_info)
        self.listbox.grid(column=0, row=1, rowspan=20)
        self.update_listbox()
        add_new_acc_btn = Button(text="Add new account", command=self.add_account, height=1, width=19,
                                 font=font.Font(family="Arial", size=20))
        add_new_acc_btn.grid(row=21, column=0)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def search_account(self, *args):
        self.listbox.delete(0, END)
        for acc in self.accounts_info.accounts_dict.values():
            if acc.name and self.var.get().lower() in acc.name.lower():
                self.listbox.insert(END, acc.name)

    def update_listbox(self):
        self.listbox.delete(0, END)
        for values in sorted(self.accounts_info.accounts_dict.values(), key=lambda acc: acc.name.lower()):
            self.listbox.insert(END, values.name)

    def add_account(self):
        new_account = self.accounts_info.add_account()
        self.edit_account(new_account)

    def get_account_info(self, event):
        sel = self.listbox.curselection()
        string = self.listbox.get(sel[0])
        account = self.accounts_info.find_account(string)
        self.update(account)

    def update(self, account):
        self.destroy_ui_items()
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
        self.destroy_ui_items()
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
        label_font = font.Font(family="Arial", size=11, weight='bold')
        account_data_font = font.Font(family="Arial", size=10)
        extra_info = Label(text='\t' + 'Extra info:', font=label_font)
        extra_info.grid(row=i, column=j, sticky='w')
        self.account_data.append(extra_info)
        extra_info_entry = Entry(font=account_data_font)
        extra_info_entry.insert(0, account.extra_info if account.extra_info else '')
        extra_info_entry.grid(row=i, column=j + 1, sticky='w')
        self.account_data.append(extra_info_entry)
        i = i + 1

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
            login_remove_btn = Button(text='Remove', command=partial(self.remove_login, (index + 1) * 2, account.id))
            login_remove_btn.grid(row=i, column=j + 2, sticky='w')
            logins.append(login_remove_btn)
            i = i + 1
        login_add_new_btn = Button(text='Add new', command=partial(self.add_new_login, account.id))
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
        for index, (opt_key, opt_val) in enumerate(account.optional.items()):
            optional_key = Entry(font=label_font)
            optional_key.insert(0, opt_key)
            optional_key.grid(row=i, column=j, sticky='w')
            optional_data = Entry(font=account_data_font)
            optional_data.insert(0, opt_val)
            optional_data.grid(row=i, column=j + 1, sticky='w')
            optional_info.append((optional_key, optional_data))
            optional_remove_btn = Button(text='Remove', command=partial(self.remove_optional, index, account.id))
            optional_remove_btn.grid(row=i, column=j + 2, sticky='w')
            optionals.append(optional_remove_btn)
            i = i + 1
        optional_add_new_btn = Button(text='Add new', command=partial(self.add_new_optional, account.id))
        optional_add_new_btn.grid(row=i, column=j + 1, sticky='w')
        optionals.append(optional_add_new_btn)
        self.account_data.append(optional_info)
        self.account_data.append(optionals)
        remove_btn = Button(text='Save', command=partial(self.save_edited_account, account.id))
        remove_btn.grid(row=21, column=j + 4, sticky='e')

    def destroy_ui_items(self):
        for it in self.account_data:
            if str(type(it)) == '<class \'dict\'>':
                for key, val in it:
                    key.destroy()
                    val.destroy()
            elif str(type(it)) == '<class \'list\'>':
                for l in it:
                    l.destroy()
            else:
                it.destroy()
        self.account_data.clear()

    def remove_account(self, account):
        if messagebox.askyesno(message="Are you sure that you want to delete account?"):
            self.accounts_info.delete_account(account.id)
            self.listbox.delete(self.listbox.get(0, END).index(account.name))
            for it in self.account_data:
                it.destroy()
            self.account_data.clear()

    def remove_login(self, index, id):
        self.account_data[6][index - 1].destroy()
        self.account_data[6][index].destroy()
        del self.account_data[6][index]
        del self.account_data[6][index - 1]
        self.update_edited_window(id)

    def add_new_login(self, id):
        self.account_data[6].insert(-1, Entry())
        self.account_data[6].insert(-1, Button())
        self.update_edited_window(id)

    def remove_optional(self, index, id):
        self.account_data[9][index][0].destroy()
        self.account_data[9][index][1].destroy()
        self.account_data[10][index + 1].destroy()
        del self.account_data[9][index]
        del self.account_data[10][index + 1]
        self.update_edited_window(id)

    def add_new_optional(self, id):
        self.account_data[9].append((Entry(), Entry()))
        self.account_data[10].insert(-1, Button())
        self.update_edited_window(id)

    def save_edited_account(self, id):
        account = self.get_edited_account(id)
        if self.accounts_info.is_name_available(account.name, id):
            self.accounts_info.update_account(account)
            self.update_listbox()
            self.update(account)
        else:
            messagebox.showerror(message=f'Account with a name \'{account.name}\' already exists')

    def update_edited_window(self, id):
        self.edit_account(self.get_edited_account(id))

    def get_edited_account(self, id):
        name = self.account_data[1].get()
        extra_info = self.account_data[3].get()
        website = self.account_data[5].get()
        login = []
        for l in self.account_data[6][1:-1:2]:
            login.append(l.get())
        password = self.account_data[8].get()
        optional = dict()
        for opt_key, opt_val in self.account_data[9]:
            optional.update({opt_key.get(): opt_val.get()})
        return Account(id, name, extra_info, website, login, password, optional)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.accounts_info.writeToXml()
            self.root.destroy()
