import random
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = available

    def getBookId(self):
        return self.__isbn
    
    def getBookTitle(self):
        return self.__title
    
    def getAvailability(self):
        return self.__available

    def markBorrowed(self):
        self.__available = False
    
    def markReturned(self):
        self.__available = True

    def show_details(self):
        print(f"Book Title: {self.__title}")
        print(f"Author Name: {self.__author}")
        print(f"Book Id: {self.__isbn}")
        print(f"Is Available: {self.__available}")

class Member:
    def __init__(self, name, member_id, borrowedList=[]):
        self.__name = name
        self.__memberId = member_id
        self.__borrowedList = borrowedList

    def getMemberId(self):
        return self.__memberId

    def getMemberName(self):
        return self.__name
    
    def show_details(self):
        print(f"Member Name: {self.__name}")
        print(f"Member Id: {self.__memberId}")
        print(f"Borrowed Book Id list: {self.__borrowedList}")

    def borrow_book(self):
        choice = int(input("If you want to search book by title: type 1\nIf you want to search book by id: type 2"))
        if choice == 1:
            book = l.searchBookByTitle()
            print(book)
            


class Library:
    books = []

    @classmethod
    def addBook(cls):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        isbn = random.randint(10**9 , 10**10 - 1)
        b = Book(title, author, isbn)
        cls.books.append(b)
        print("Book Successfully added to library.")
        print("Book Details are: ")
        b.show_details()
    
    @classmethod
    def removeBook(cls):
        isbn = int(input("Enter the Book id to remove: "))
        for book in cls.books:
            if book.getBookId() == isbn:
                cls.books.remove(book)
                print("Book reomoved Successfully.")
                break
        else:
            print("Book Not Found.")

    @classmethod 
    def searchBookByTitle(cls):
        title = input("Enter Book title: ").lower()
        for book in cls.books:
            if book.getTitle().lower() == title:
                return book
        else:
            print("Book Not found.")

    @classmethod
    def searchBookByIsbn(cls):
        isbn = int(input("Enter Book title: "))
        for book in cls.books:
            if book.getBookId() == isbn:
                return book
        else:
            print("Book Not found.")

    @classmethod
    def listOfBooks(cls):
        if len(cls.books)!=0:
            print("List of Books:")
            for book in cls.books:
                book.show_details()
        else:
            print("Library is empty.")

class Manager:
    members = []

    @classmethod
    def addMember(cls):
        name = input("Enter Member name: ")
        memberId = random.randint(10**5 , 10**6 - 1)
        u = Member(name, memberId)
        cls.members.append(u)
        print("Member Added Successfully.")
        print("Member Details are: ")
        u.show_details()
    
    @classmethod
    def removeMember(cls):
        memberId = int(input("Enter Member Id to remove: "))
        for member in cls.members:
            if member.getMemberId == memberId:
                cls.books.remove(member)
                print("Member reomoved Successfully.")
                break
        else:
            print("Member Not Found.")
    
    @classmethod
    def searchMemmberById(cls):
        memberId = int(input("Enter Member Id: "))
        for member in cls.members:
            if member.getMemberId() == memberId:
                print("Member Found.")
                member.show_details()
                break
        else:
            print("Member Not found.")

l = Library()
l.addBook()
l.addBook()

m.borrow_book()