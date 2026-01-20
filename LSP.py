class Vehicle:
    def move(self):
        pass

class Bike(Vehicle):
    def move(self):
        print("Bike runs on road")
    
class Boat(Vehicle):
    def move(self):
        print("Boat runs on water")

v = Vehicle()
b = Bike()
b1 = Boat()
b1.move()