class User(object):
    # the __init__ method is called every time a new object is created.
    def __init__(self, name, email):
    # set some instance variables. Just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help a user login
    def login(self):
        self.logged = True
        print self.name + "Is logged in."
        return self
    # now create an instance of the class
    def logout(self):
        slef.logged = False
        print self.name + "is not logged in"
        return self
    def show(self):
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self
