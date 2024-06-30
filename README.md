**Low Level System Design Practice**


**Problem Statement: Library Management System**


**Description**

This project is a simple Library Management System implemented in Python, designed to manage a collection of books and users. The system allows users to borrow and return books and provides mechanisms to track which books are currently borrowed and by whom. The project demonstrates key Object-Oriented Programming (OOP) concepts such as inheritance, polymorphism, abstraction, and encapsulation.

**Classes and Their Responsibilities**




**LibraryItem**


      Represents items that can be borrowed from the library.
      
      Attributes: name, dueDate, fine.
      
      Method: getImpDetails(), which returns a string with item details.




**Book (Inherits LibraryItem)**


      Represents a book in the library.
    
      Additional Attributes: publication, genre.
      
      Overrides the __str__ method to provide details specific to books.



**LibraryUser**


      Represents a user of the library.
      
      Attributes: username, email.
      
      Methods: getUserDetails(), which returns user details, and __str__ to return a string representation.
  


**Student (Inherits LibraryUser)**

      Represents a student user of the library.
      
      Additional Attributes: firstName, lastName, borrowedBookList.
      
      Methods: getBorrowedBooksDetails(), borrowHistory(), and __str__ to return a string representation.


**LibraryMain**


      Manages the main library operations such as adding users, adding books, displaying all users, books, and borrowed books.
      
      Methods: addUsers(), showActiveUsers(), addItems(), showAllBooks(), showBorrowedBooks(), enterNewBook(), enterDetails(), borrowBooks(), and returnBooks().
      



**StartProgram**

      Contains the main program loop to interact with the library system through a command-line interface.


**Here is how you can run the main program:**

      from StartProgram import main
      main()


This project provides a basic framework for a Library Management System, demonstrating fundamental OOP principles and offering a foundation for further development and customization.
