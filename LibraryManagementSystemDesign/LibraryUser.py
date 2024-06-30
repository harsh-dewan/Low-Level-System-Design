class LibraryUser(object):

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def getUserDetails(self):
        return f"Username: {self.username} | UserEmail: {self.email}"