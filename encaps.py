class Encapsulation:
        
    def sound(self):
        print("makes sound")

class Child(Encapsulation):
    def sound(self):
        super().sound()
        print("childs sound")
     
    def angry(self):
        
        self.sound()


c = Child()
c.angry()