class LibraryItem(object):
    """
        this represents all the items which can be borrowed from the library
        our current scope is for books only, but it can include other items like game,
        any electronic item, basically anything which the library offers to lend
    """

    def __init__(self, name, dueDate, fine):
        self.name = name
        self.dueDate = dueDate
        self.fine = fine

    def getImpDetails(self):
        return (f"Item Borrowed: {self.name} | Item DueDate: {self.dueDate} "
                f"| Item Fine After Due Date {self.fine}")
