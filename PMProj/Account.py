class Account:


    def __init__(self, id, name, extra_info, website, login, password, optional):
        self.id = id
        self.name = name
        self.extra_info = extra_info
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
