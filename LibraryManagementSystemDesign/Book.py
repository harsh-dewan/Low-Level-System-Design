from LibraryItem import LibraryItem


class Book(LibraryItem):

    def __init__(self, name, dueDate, fine, publication, genre):
        super().__init__(name, dueDate, fine)
        self.publication = publication
        self.genre = genre

    def __str__(self):
        return self.getImpDetails() + f"{"Book Publication " | self.publication | " Book Genre: " | self.genre }"
