#getters and setters
class Bank:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        print(f"Balance is {self.__balance}")
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative. ERROR")

b = Bank(5000)
b.get_balance()
b.set_balance(4000)
b.get_balance()
b.set_balance(-674564)
b.get_balance()

#method overloading
class Calc:
    def multiply(self, a, b, c=1):
        print(a*b*c)
    
c = Calc()
c.multiply(6,9)
c.multiply(8,5,4)

#abstract class
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calc_salary(self, hours, rate):
        return f"Salary is : {hours*rate} rupees"

class Manager(Employee):
    def calc_salary(self, hours, rate):
        return super().calc_salary(hours, rate)

m = Manager()
print(m.calc_salary(8,300))

#concept rivisons
#Class showing basic object creation
class C_1:
    pass

c = C_1()

#Class using constructor + instance methods
class C_2:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)

c = C_2("madan")
c.show()

#Two classes showing inheritance & super()
class P:
    def __init__(self):
        pass

class C(P):
    def __init__(self):
        super().__init__()

#Two classes showing polymorphism (same method, different behavior)
class P:
    def sound(self):
        print("P makes sound")
    
class C(P):
    def sound(self):
        print("C makes sound")

c = C()
c.sound()

#Class with private variables + getter & setter methods
class c_5:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        print(self.__age)
    
    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age

c5 =c_5(20)
c5.get_age()
c5.set_age(30)
c5.get_age()


class Employee:
    company_name = "TechVerse Pvt Ltd"   # class variable

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ₹{self.salary}")
        print(f"Company: {Employee.company_name}")

    @classmethod
    def update_company_name(cls, new_name):
        cls.company_name = new_name
        print(f"Company name updated to: {cls.company_name}")


# Testing
e1 = Employee("Madan", 108, 50000)
e2 = Employee("Kiran", 205, 65000)

e1.show_details()
print()

Employee.update_company_name("AI Future Systems")
print()

e2.show_details()
