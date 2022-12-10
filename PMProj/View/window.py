import enum
from tkinter import Label
import tkinter as tk
from tkinter import messagebox


class Window:
    def __init__(self, *args):
        self.root = tk.Tk()
        self.root.columnconfigure(2, {f'minsize': self.root.winfo_screenwidth() / 2})
        self.root.geometry("%dx%d" % (self.root.winfo_screenwidth()/2, self.root.winfo_screenheight()/2))
        self.name = Label(text="Name:")
        self.name.grid(row=1, column=2, sticky = 'w')
        self.website = Label(text="Website:")
        self.website.grid(row=2, column=2, sticky = 'w')
        self.login = Label(text="Login:")
        self.login.grid(row=3, column=2, sticky = 'w')
        self.password = Label(text="Password:")
        self.password.grid(row=4, column=2, sticky = 'w')

    def update(self, account):
        self.name['text'] = f'\tName:\t\t{account.name}'
        self.website['text'] = f'\tWebsite:\t\t{account.website}'
        self.login['text'] = f'\tLogin:\t\t{account.login}'
        self.password['text'] = f'\tPassword:\t{account.password}'
        self.root.mainloop()
