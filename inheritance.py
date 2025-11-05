class Vehicle:
    def start(self):
        print("Vehicle started.")

class Bike(Vehicle):
    def ride(self):
        print("Riding a bike.")

b = Bike()
b.start()
b.ride()

class Person:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
    
    def display(self):
        super().display()
        print(f"Roll No: {self.roll_no}")

s1 = Student("Devru", 108)
s1.display()

#task from gpt
class Vehicle:
    def __init__(self,b,m):
        self.brand = b
        self.model = m

    def show_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}")

class Car(Vehicle):
    def __init__(self, b, m, p):
        super().__init__(b, m)
        self.price = p
    
    def show_info(self):
        super().show_info()
        print(f"Price: {self.price}")

c = Car("BMW","2024",23000000)
c.show_info()