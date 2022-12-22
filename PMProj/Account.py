class Account:
    def __init__(self, name, website, login, password, optional):
        self.name = name
        self.website = website
        self.login = login
        self.password = password
        self.optional = optional

    def get_info(self):
        print("name: ", str(self.name))
        print("website: ", str(self.website))
        print("login: ", str(self.login[0]))
        print("password: ", str(self.password))
        print(self.optional.keys(), self.optional.values())