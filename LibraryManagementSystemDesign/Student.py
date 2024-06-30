from LibraryUser import LibraryUser


class Student(LibraryUser):

    def __init__(self, username, email, firstName, lastName, borrowedBookList=[]):
        super().__init__(username, email)
        self.firstName = firstName
        self.lastName = lastName
        self.borrowedBookList = borrowedBookList
        self.borrowHistoryList = []

    def __str__(self):
        return self.getUserDetails() + f"| FirstName {self.firstName} | LastName: {self.lastName} "

    def getBorrowedBooksDetails(self):
        return self.borrowedBookList.__str__()

    def borrowHistory(self):
        return self.borrowHistoryList.__str__()
