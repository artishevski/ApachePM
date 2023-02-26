class Account:

    def __init__(self, id, name = '', starred = False, extra_info='', website='', login=list(), password='', optional=dict()):
        self.id = id
        self.name = name
        self.starred = starred
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
