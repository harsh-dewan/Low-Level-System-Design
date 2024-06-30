from Book import Book
from Student import Student


class LibraryMain(object):
    """
    Library will have name and its city
    here I need two things:
        1. list of the all the items which can be borrowed, currently books
        2. list of all the active users in the library
    """

    def __init__(self, name, city, bookDict={}, userDict={}, borredBooks={}):
        self.name = name
        self.city = city
        self.libraryBooksDict = bookDict  #list of all the books available in library
        self.borrowedBooksDict = borredBooks #list of all the borrowed books at any time
        self.activeUsersDict = userDict   #list of all the active Users

    def addUsers(self):
        user = self.enterDetails(self)
        self.activeUsersDict[user.username] = user.__str__()

    def showActiveUsers(self):
        if len(self.activeUsersDict) == 0:
            print("No active users")
            return
        return self.activeUsersDict.__str__()

    def addItems(self):
        book = self.enterNewBook(self)
        self.libraryBooksDict[book.name] = book.__str__()

    def showAllBooks(self):
        if len(self.libraryBooksDict) == 0:
            print("No books available")
            return
        return self.libraryBooksDict.__str__()

    def showBorrowedBooks(self):
        if len(self.borrowedBooksDict) == 0:
            return "No borrowed books found!"
        return self.borrowedBooksDict.__str__()

    @staticmethod
    def enterDetails(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        firstName = input("Enter first name ")
        lastName = input("Enter last name ")
        newStudent = Student(username, email, firstName, lastName)
        return newStudent

    @staticmethod
    def enterNewBook(self):
        name = input("Enter the name of the book: ")
        dueDate = input("Enter due date: ")
        fine = input("Fine in USD ")
        publication = input("publication: ")
        genre = input("Genre: ")
        newBook = Book(name, dueDate, fine, publication, genre)
        return newBook

    def borrowBooks(self):
        """
        1. select user
        2. select books (currently we are not checking if the book is available or not)
        3. update required lists
        """
        if len(self.activeUsersDict) == 0:
            print("No active users, please add some users first")
            return
        if len(self.libraryBooksDict) == 0:
            print("No books available, please add some books first")
            return
        username = input("Enter the username: ")
        bookname = input("Enter the bookname ")
        self.borrowedBooksDict[bookname] = {
                "userdetails": self.activeUsersDict[username],
                "bookdetails":self.libraryBooksDict[bookname]
            }
        return

    def returnBooks(self):
        if len(self.borrowedBooksDict) == 0:
            return "No borrowed books found!"
        username = input("Enter the username: ")
        bookname = input("Enter the bookname ")
        del self.borrowedBooksDict[bookname]
        pass
