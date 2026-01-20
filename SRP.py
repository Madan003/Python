class Book:
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn

class Display:
    def display(self,book):
        print(f"Book Name: {book.name}")
        print(f"Author: {book.author}")
        print(f"Book Number: {book.isbn}")

b = Book("Bengaluru today","Mr Gowda",159632478)
d = Display()
d.display(b)