class Student:
    def __init__(self, name, usn, branch, sem, year):
        self.name = name
        self.usn = usn
        self.branch = branch
        self.sem = sem
        self.year = year
        self.__marks = {}
    
    def get_usn(self):
        return self.usn
    
    def calc_percentage(self):
        total_marks = sum(self.__marks.values())
        if len(self.__marks) > 0:
            return round((total_marks/(len(self.__marks)*100))*100,2)
        else:
            return 0
    
    def calc_grade(self):
        total_marks = sum(self.__marks.values())
        if len(self.__marks) > 0:
            percentage = (total_marks/(len(self.__marks)*100))*100
        else:
            percentage = 0
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B+"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C+"
        elif percentage >= 35:
            return "C"
        else:
            return "Fail"
        
    def add_marks(self, subject, marks):
        self.__marks[subject] = marks
    
    def is_passed(self):
        is_passed = all(mark>=35 for mark in self.__marks.values())
        if is_passed:
            return "Pass"
        else:
            return "Fail"
    
    def display_marks(self):
        if len(self.__marks) > 0:
            print("Subject - Marks")
        for sub, mark in self.__marks.items():
            print(f"{sub} - {mark}")

class Generate_Report:
    CSE = []
    ISE = []
    @classmethod
    def add_student(cls):
        name = input("Enter student name: ")
        branch = input("Enter student branch: ")
        sem = input("Enter student semester: ")
        year = input("Enter student year: ")
        if branch.lower() == "cse":
            usn = len(cls.CSE) + 1
            s = Student(name,usn,branch,sem,year)
            cls.CSE.append(s)
            print("Student added successfully.")
        elif branch.lower() == "ise":
            usn = len(cls.ISE) + 1
            s = Student(name,usn,branch,sem,year)
            cls.ISE.append(s)
            print("Student added successfully.")
        print("Student Deatils: ")
        print(f"Name: {name}")
        print(f"USN: {usn}")
        print(f"Branch: {branch}")
        print(f"Sem: {sem}")
        print(f"Year: {year}")

    @classmethod
    def add_marks(cls):
        branch = input("Enter student branch: ")
        if branch.lower() == "cse":
            usn = int(input("Enter student university seat number: "))
            for student in cls.CSE:
                if usn == student.get_usn():
                    subject = input("Enter the subject name: ")
                    marks = int(input("Enter the marks: "))
                    student.add_marks(subject, marks)
                    print("Marks added successfully.")
                    break
            else:
                print("Student not found.")
        elif branch.lower() == "ise":
            usn = int(input("Enter student university seat number: "))
            for student in cls.ISE:
                if usn == student.get_usn():
                    subject = input("Enter the subject name: ")
                    marks = int(input("Enter the marks: "))
                    student.add_marks(subject, marks)
                    print("Marks added successfully.")
                    break
            else:
                print("Student not found.")
    
    @classmethod
    def get_report_card(cls):
        branch = input("Enter student branch: ")
        if branch.lower() == "cse":
            usn = int(input("Enter student university seat number: "))
            for student in cls.CSE:
                if usn == student.get_usn():
                    print("------- Report Card ------")
                    print("------- 2025-26 ----------")
                    print(f"Name: {student.name}")
                    print(f"USN: {student.usn}")
                    print(f"Branch: {student.branch}")
                    print(f"Sem: {student.sem}")
                    print(f"Year: {student.year}")
                    student.display_marks()
                    print(f"Percentage: {student.calc_percentage()}")
                    print(f"Grade: {student.calc_grade()}")
                    print(f"Result: {student.is_passed()}")
                    print("--------------------------")
                    break
            else:
                print("Student not found.")
        elif branch.lower() == "ise":
            usn = int(input("Enter student university seat number: "))
            for student in cls.ISE:
                if usn == student.get_usn():
                    print("------- Report Card ------")
                    print("------- 2025-26 ----------")
                    print(f"Name: {student.name}")
                    print(f"USN: {student.usn}")
                    print(f"Branch: {student.branch}")
                    print(f"Sem: {student.sem}")
                    print(f"Year: {student.year}")
                    student.display_marks()
                    print(f"Percentage: {student.calc_percentage()}")
                    print(f"Grade: {student.calc_grade()}")
                    print(f"Result: {student.is_passed()}")
                    print("--------------------------")
                    break
            else:
                print("Student not found.")

    @classmethod
    def display_students(cls):
        branch = input("Enter student's branch: ")
        if branch.lower() == "cse":
            if len(cls.CSE) > 0:
                for student in cls.CSE:
                    print(f"{student.usn} - {student.name}")
            else:
                print("Student list is empty.")
        elif branch.lower() == "ise":
            if len(cls.ISE) > 0:
                for student in cls.ISE:
                    print(f"{student.usn} - {student.name}")
            else:
                print("Student list is empty.")
   
def menu():
    print("--- Madan Gowda University, Shivamogga ---")
    print("1. Add Student")
    print("2. Get Report card")
    print("3. Add Marks")
    print("4. Display student list")
    print("5. Exit")

teacher = Generate_Report()
while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1: teacher.add_student()
    elif choice == 2: teacher.get_report_card()
    elif choice == 3: teacher.add_marks()
    elif choice == 4: teacher.display_students()
    elif choice == 5: break
    else:
        print("Oh no! Invalid choice, Please enter a valid choice.")