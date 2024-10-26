from abc import abstractmethod

class Pritable (ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Pritable):
    def __init__(self,title, author):
        self.title=title
        self.author=author
    def print_info(self):
        print(f"Book:{self.title} by {self.author}")

book=Book("The great gatsby", "F.Scott Fitzgerald")
book.print_info()