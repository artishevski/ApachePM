class Account:
    def __init__(self, name, website, login, password, optional):
        self.name = name
        self.website = website
        self.login = list()
        for i in login:
            self.login.append(i)
        self.password = password
        self.optional = dict()
        for key, val in optional:
            self.optional.update({key: val})

    def get_info(self):
        print("name: ", str(self.name))
        print("website: ", str(self.website))
        print("login: ", str(self.login[0]))
        print("password: ", str(self.password))
        print(self.optional.keys(), self.optional.values())