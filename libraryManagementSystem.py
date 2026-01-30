import random
import datetime
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

    def showDetails(self):
        print(f"Book Title: {self.__title}")
        print(f"Author Name: {self.__author}")
        print(f"Book Id: {self.__isbn}")
        print(f"Is Available: {self.__available}")

class User:
    def __init__(self, name, user_id):
        self.__name = name
        self.__userID = user_id
        self.__borrowedList = []

    def getUserId(self):
        return self.__userID

    def getUserName(self):
        return self.__name
    
    def getBorrowedList(self):
        return self.__borrowedList
    
    def showDetails(self):
        print(f"User Name: {self.__name}")
        print(f"User Id: {self.__userID}")
        print(f"Borrowed Book Id list: {self.__borrowedList}")

    def borrowBook(self, bookId):
        time = datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")
        self.__borrowedList.append([bookId, time])

    def returnBook(self, bookId):
        for borrowedList in self.__borrowedList:
            if borrowedList[0] == bookId:
                borrowed = borrowedList[1]
                fmt = "%d:%m:%Y %H:%M:%S"
                borrowedTime = datetime.datetime.strptime(borrowed,fmt)
                returnTime = datetime.datetime.now()
                diff = returnTime - borrowedTime
                seconds = diff.total_seconds()
                hours = seconds/3600
                bill = round(hours * 29,2)
                print(f"Based on your borrowed time {diff} your bill is {bill}rupees")
                print("Pleasse pay the bill and return book.")
                amount = float(input("Enter your bill amount to pay: "))
                if amount == bill:
                    print("Bill Paid Successfully.")
                    self.__borrowedList.remove(borrowedList)
                    print("Book Returned Successfully. Thank you!")
                    break
                else:
                    print("Please pay the bill then return!!!")
                    break
        else:
            print("You didn't borrowed this book!, please check once.")

class Library:
    books = []
    users = []

    @classmethod
    def addBook(cls):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        isbn = random.randint(10**9 , 10**10 - 1)
        b = Book(title, author, isbn)
        cls.books.append(b)
        print("Book Successfully added to library.")
        print("Book Details are: ")
        b.showDetails()
    
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
            if book.getBookTitle().lower() == title:
                print("Book Found.")
                return book.showDetails()
        else:
            print("Book Not found.")

    @classmethod
    def searchBookByIsbn(cls):
        isbn = int(input("Enter Book ID: "))
        for book in cls.books:
            if book.getBookId() == isbn:
                print("Book Found.")
                return book.showDetails()
        else:
            print("Book Not found.")

    @classmethod
    def listOfBooks(cls):
        if len(cls.books)!=0:
            print("List of Books:")
            for book in cls.books:
                book.showDetails()
                print("-------------------------")
        else:
            print("Library is empty.")

    @classmethod
    def addUser(cls):
        name = input("Enter user name: ")
        user_id = random.randint(10**4,10**5)
        u = User(name, user_id)
        cls.users.append(u)
        print("User created Successfully.")
        print("User Details are: ")
        u.showDetails()

    @classmethod
    def removeUser(cls):
        user_id = int(input("Enter user ID to remove: "))
        for user in cls.users:
            if user.getUserId() == user_id:
                cls.users.remove(user)
                print("User Removed Successfully.")
                break
        else:
            print("User Not found.")

    @classmethod
    def listOfUsers(cls):
        if(len(cls.users)!=0):
            print("User List: ")
            for user in cls.users:
                user.showDetails()
                print("-------------------------")
        else:
            print("User List is empty.")
    
    @classmethod
    def borrowBook(cls):
        user_id = int(input("Enter your user ID: "))
        for user in cls.users:
            if user.getUserId() == user_id:
                book_id = int(input("Enter the book id you want to borrow: "))
                for book in cls.books:
                    if book.getBookId() == book_id:
                        if book.getAvailability() == True:
                            book.markBorrowed()
                            user.borrowBook(book_id)
                            print("Book Borrowed Successfully.")
                        else:
                            print("Sorry!, Book was already borrowed by someone.")
                        break
                else:
                    print("Book not found!.")
                break
        else:
            print("User not found!, you can't borrow a book.")

    @classmethod
    def returnBook(cls):
        user_id = int(input("Enter your user ID: "))
        for user in cls.users:
            if user.getUserId() == user_id:
                book_id = int(input("Enter the book id you want to return: "))
                for book in cls.books:
                    if book.getBookId() == book_id:
                        return_time = datetime.datetime.now()
                        borrowedList = user.getBorrowedList()

                        user.returnBook(book_id)
                        book.markReturned()
                        
                        break
                else:
                    print("Book not found!")
                break
        else:
            print("User not found!.")
    
    @classmethod
    def listOfAvailableBooks(cls):
        if len(cls.books)!=0:
            is_available = any(book.getAvailability() == True for book in cls.books)
            if is_available == True:
                print("List of Available Books:")
                for book in cls.books:
                    if book.getAvailability() == True:
                        book.showDetails()
                        print("-------------------------")
            else:
                print("Sorry!, Books are Unavailable at this Moment.")
        else:
            print("Books list is empty.")

    @classmethod
    def listOfBorrowedBooks(cls):
        if len(cls.books)!=0:
            is_available = any(book.getAvailability() == False for book in cls.books)
            if is_available == True:
                print("List of Borrowed Books:")
                for book in cls.books:
                    if book.getAvailability() == False:
                        book.showDetails()
                        print("-------------------------")
            else:
                print("Borrowed Book list is empty, All Books are Available.")
        else:
            print("Books list is empty.")

def menu():
    print("------ Madan Gowda Library, Bengaluru ------")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by Title")
    print("4. Search Book by Book ID")
    print("5. List of Books")
    print("6. List of Available Books")
    print("7. List of Borrowed Books")
    print("8. Add User")
    print("9. Remove User")
    print("10. List of Users")
    print("11. Borrow Book")
    print("12. Return Book")
    print("13. Exit")

l = Library()
# TODO: jgjfns gh
while True:
    menu()
    choice = int(input("Enter your choice(1-11): "))
    if choice == 1: l.addBook()
    elif choice == 2: l.removeBook()
    elif choice == 3: l.searchBookByTitle()
    elif choice == 4: l.searchBookByIsbn()
    elif choice == 5: l.listOfBooks()
    elif choice == 6: l.listOfAvailableBooks()
    elif choice == 7: l.listOfBorrowedBooks()
    elif choice == 8: l.addUser()
    elif choice == 9: l.removeUser()
    elif choice == 10: l.listOfUsers()
    elif choice == 11: l.borrowBook()
    elif choice == 12: l.returnBook()
    elif choice == 13:
        print("Thank You!") 
        break