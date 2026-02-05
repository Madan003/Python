class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__rollno = roll_no
        self.__marks = marks
    
    def calculate_grade(self):
        grade = sum(self.__marks)/len(self.__marks)
        if grade>=90: return "O"
        elif grade>=75: return "A"
        elif grade>=50: return "B"
        elif grade>=35: return "C"
        else: return "F"
    
    def set_name(self, name):
        self.__name = name
    
    def set_marks(self, marks):
        self.__marks = marks 
    
    def get_rollno(self):
        return self.__rollno

    def get_name(self):
        print(f"Name: {self.__name}")

    def get_marks(self):
        print(f"Marks: {self.__marks}")   

    def show_details(self):
        print(f"Name: {self.__name}")
        print(f"Roll No: {self.__rollno}") 
        print(f"Marks: {self.__marks}") 
        print(f"Grade: {self.calculate_grade()}")

class StudentManager:
    student_list = []

    @classmethod
    def add_student(cls):
        name = input("Enter Student Name: ")
        roll_no = int(input("Enter Student Roll No: "))
        marks = [int(item) for item in input("Enter Student marks(space sepearatedly): ").split()]
        while True:
            if len(marks) == 0:
                print("Student marks should not be empty.")
                marks = [int(item) for item in input("Enter Student marks(space sepearatedly): ").split()]
            else:
                break
        s = Student(name, roll_no, marks)
        if len(cls.student_list) == 0:
            cls.student_list.append(s)
            print("Student Added Successfully.")
        else:
            found = False
            for student in cls.student_list:
                if student.get_rollno() == roll_no:
                    found = True
                    break
            if found:
                print("Student with this roll No already Found in Student List.")
            else:
                cls.student_list.append(s)
                print("Student Added Successfully.")
    
    @classmethod
    def remove_student(cls):
        roll_no = int(input("Enter the Student Roll No to remove: "))
        for student in cls.student_list:
            if student.get_rollno() == roll_no:
                cls.student_list.remove(student)
                print("Student Removed Successfully.")
                break
        else:
            print("Student Not found.")
    
    @classmethod
    def search_student(cls):
        roll_no = int(input("Enter the Student Roll No to Search: "))
        for student in cls.student_list:
            if student.get_rollno() == roll_no:
                print("Student Found: ")
                student.show_details()
                break
        else:
            print("Student Not found.")

    @classmethod
    def update_student(cls):
        roll_no = int(input("Enter the Student Roll No to Update: "))
        for student in cls.student_list:
            if student.get_rollno() == roll_no:
                name = input("Enter Student Name: ")
                marks = [int(item) for item in input("Enter Student marks(space sepearatedly): ").split()]
                student.set_name(name)
                student.set_marks(marks)
                print("Student Data Updated Successfully.")
                break
        else:
            print("Student Not found.")

    @classmethod
    def show_all_students(cls):
        if len(cls.student_list) == 0:
            print("Students List is empty")
        else:
            print("-----Students Lists-----")
            for student in cls.student_list:
                student.show_details()
                print("-----------")
    
    
m = StudentManager()
m.loadStudents()
while True:
    print("---------***---------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")
    print("---------***---------")
    operation = int(input("Manager Please enter the option to perform operation: "))
    if operation == 1: m.add_student()
    elif operation == 2: m.show_all_students()
    elif operation == 3: m.update_student()
    elif operation == 4: m.search_student()
    elif operation == 5: m.remove_student()
    elif operation == 6: 
        print("Thank You!")
        break