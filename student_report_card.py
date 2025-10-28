class Student:
    def __init__(self, name="unknown", roll_number=0, marks=0):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def calculate_total(self):
        return sum(self.marks)
    
    def calculate_percentage(self):
        return round((sum(self.marks)/(len(self.marks)*100))*100,2)
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_number}")
        print(f"Total marks: {self.calculate_total()}")
        print(f"Percentage: {self.calculate_percentage()}%")

students = Student("Madan",108,[95,85,76,88,92])
students.display_details()