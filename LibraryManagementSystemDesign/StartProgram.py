from LibraryMain import  LibraryMain


def main():
    print("Welcome to the Leddy Library Management system Windsor")
    mylib = LibraryMain("LeddyLibrary", "Windsor")
    while True:
        print("**************************************************")
        print("Enter 1 to list all the users")
        print("Enter 2 to list all the books")
        print("Enter 3 to list all the borrowed books")
        print("Enter 4 to borrow a book ")
        print("Enter 5 to return a book ")
        print("Enter 6 to add users ")
        print("Enter 7 to add books ")
        option = int(input("Enter your choice from 1 to 7 only: "))
        if option == 1:
            print("All Users: ", mylib.showActiveUsers())
        elif option == 2:
            print("All Books: ", mylib.showAllBooks())
        elif option == 3:
            print("All Borrowed Books ", mylib.showBorrowedBooks())
        elif option == 4:
            mylib.borrowBooks()
            print("Book borrowed successfully")
        elif option == 5:
            mylib.returnBooks()
            print("Book returned successfully")
        elif option == 6:
            mylib.addUsers()
            print("User added successfully")
        elif option == 7:
            mylib.addItems()
            print("Books added successfully")
        else:
            print("Please enter correct option!")
    return


main()