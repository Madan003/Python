#task1
class Mobile:

    #attributes
    def __init__(self,name,price):
        self.name = name
        self.price = price

    #method
    def display_info(self):
        print(f"Mobile name is: {self.name} and price is: {self.price}")
    
mob1 = Mobile("Iqoo neo 7",28999)
mob2 = Mobile("Vivo y15",14999)

mob1.display_info()
mob2.display_info()

#task 2
class Movie:
    def __init__(self,title,ratings):
        self.title = title
        self.ratings = ratings

    def display(self):
        print(f"Movie name: {self.title}, ratings: {self.ratings}")

m1 = Movie("KGF",4.8)
m2 = Movie("Katera",4.6)
m3 = Movie("kantara",4.7)

m1.display()
m2.display()
m3.display()

#task3 with default parameters value
class Employee:
    def __init__(self, name, designation, salary=30000.00):
        self.name = name
        self.designation = designation
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}, Design: {self.designation}, Salary: {self.salary}")

e1 = Employee("Madan","Software Developer",89999.00)
e2 = Employee("Jeevan","Error Developer")
e3 = Employee("Gagan","Apna Developer",100000000.00)
e4 = Employee("Kiran","Backend Developer")

e1.display()
e2.display()
e3.display()
e4.display()