import json
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

    def show_details(self):
        print(f"Name: {self.__name}")
        print(f"Roll No: {self.__rollno}") 
        print(f"Marks: {self.__marks}") 
        print(f"Grade: {self.calculate_grade()}")

class StudentManager:
    student_list = []
    data = {}

    @classmethod
    def takeInput(cls):
        name = input("Enter Student Name: ")
        roll_no = int(input("Enter Student Roll No: "))
        marks = [int(item) for item in input("Enter Student marks(space sepearatedly): ").split()]
        return name, roll_no, marks
    
    @classmethod
    def loadJson(cls):
        try:
            with open("students.json") as file:
                cls.data = json.load(file)
            for student in cls.data["students"]:
                name = student["name"]
                rollno = student["rollNum"]
                marks = student["marks"]
                s = Student(name, rollno, marks)
                cls.student_list.append(s)
        except FileNotFoundError:
            cls.data = {"students":[]}
        
    @classmethod
    def saveFile(cls):
        try:
            with open("students.json",'w') as file:
                    json.dump(cls.data, file, indent=2)
        except Exception as e:
            print(f'Error in saving file: {e}')

    @classmethod
    def add_student(cls):
        try:
            name, roll_no, marks = cls.takeInput()
            while True:
                if len(marks) == 0:
                    print("Student marks should not be empty.")
                    marks = [int(item) for item in input("Enter Student marks(space sepearatedly): ").split()]
                else:
                    break
            s = Student(name, roll_no, marks)
            found = False
            for student in cls.student_list:
                if student.get_rollno() == roll_no:
                    found = True
                    break
            if found:
                print("Student with this roll_Num already Found in Student List.")
            else:
                cls.student_list.append(s)
                cls.data["students"].append({
                "name":name,
                "rollNum":roll_no,
                "marks": marks
            })
                cls.saveFile()
                print("Student Added Successfully.")
        except ValueError:
            print("Please Enter Correct Details!!")
    
    @classmethod
    def remove_student(cls):
        try:
            roll_no = int(input("Enter the Student Roll No to remove: "))
            for student_obj in cls.student_list:
                if student_obj.get_rollno() == roll_no:
                    cls.student_list.remove(student_obj)
                    for student_record in cls.data["students"]:
                        if student_record["rollNum"] == roll_no:
                            cls.data["students"].remove(student_record)
                            cls.saveFile()
                            break
                    print("Student Removed Successfully.")
                    break
            else:
                print("Student Not found.")
        except ValueError:
            print("Please Enter Correct Details!!")
    
    @classmethod
    def search_student(cls):
        try:
            roll_no = int(input("Enter the Student Roll No to Search: "))
            for student in cls.student_list:
                if student.get_rollno() == roll_no:
                    print("Student Found: ")
                    student.show_details()
                    break
            else:
                print("Student Not found.")
        except ValueError:
            print("Please Enter Correct Details!!")

    @classmethod
    def update_student(cls):
        try:
            roll_no = int(input("Enter the Student Roll No to Update: "))
            for student in cls.student_list:
                if student.get_rollno() == roll_no:
                    name = input("Enter Student Name: ")
                    marks = [int(item) for item in input("Enter Student marks(space sepearatedly): ").split()]
                    student.set_name(name)
                    student.set_marks(marks)
                    for student in cls.data["students"]:
                        if student["rollNum"] == roll_no:
                            student["name"] = name
                            student["marks"] = marks
                            cls.saveFile()
                    print("Student Data Updated Successfully.")
                    break
            else:
                print("Student Not found.")
        except ValueError:
            print("Please Enter Correct Details!!")

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
m.loadJson()
while True:
    try:
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
        else: print("Invalid Choice!")
    except ValueError:
            print("Please Enter Correct Details!!")