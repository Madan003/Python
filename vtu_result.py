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
    
    def add_marks(self):
        ADA = int(input("Enter the marks of Analysis & Design of Algorithms: "))
        self.__marks["ADA"] = ADA
        MC = int(input("Enter the marks of Microcontrollers: "))
        self.__marks["MC"] = MC
        DBMS = int(input("Enter the marks of Database & Management System: "))
        self.__marks["DBMS"] = DBMS
        ADAL = int(input("Enter the marks of Analysis and Design of Algorithms LAB: "))
        self.__marks["ADAL"] = ADAL
        DMS = int(input("Enter the marks of Discrete Mathematical Structures: "))
        self.__marks["DMS"] = DMS
        BIO = int(input("Enter the marks of Biology for Engineers: "))
        self.__marks["BIO"] = BIO
        UHV = int(input("Enter the marks of Universal Human values course: "))
        self.__marks["UHV"] = UHV
        UI_UX = int(input("Enter the marks of UI/UX: "))
        self.__marks["UI_UX"] = UI_UX
        print("Marks added successfully.")
    
    def calc_percentage(self):
        total_marks = sum(self.__marks.values())
        if len(self.__marks) > 0:
            return round((total_marks/(len(self.__marks)*100))*100,2)
        else:
            return 0
        
    def calc_grade_credits(self):
        # grade * credits of each subject
        credit = [3,4,4,1,3,2,1,1]
        grade_credits = []
        i = 0
        for mark in self.__marks.values(): 
            if mark >= 90:
                grade_credits.append(credit[i]*10)
            elif mark >= 80:
                grade_credits.append(credit[i]*9)
            elif mark >= 70:
                grade_credits.append(credit[i]*8)
            elif mark >= 60:
                grade_credits.append(credit[i]*7)
            elif mark >= 50:
                grade_credits.append(credit[i]*6)
            elif mark >= 40:
                grade_credits.append(credit[i]*5)
            elif mark >= 30:
                grade_credits.append(credit[i]*4)
            elif mark >= 20:
                grade_credits.append(credit[i]*3)
            elif mark >= 10:
                grade_credits.append(credit[i]*2)
            elif mark >= 0:
                grade_credits.append(credit[i]*1)
            i += 1
        return grade_credits

    def calc_sgpa(self):
        total_credits = 19
        grade_credits = Student.calc_grade_credits(self)
        sgpa = round(sum(grade_credits)/total_credits,2)
        return sgpa
    
    def is_passed(self):
        is_passed = False
        is_passed = all(mark>=35 for mark in self.__marks.values())
        if is_passed == True:
            return "Pass"
        else:
            return "Fail"
    
    def display_marks(self):
        credit = [3,4,4,1,3,2,1,1]
        grade_credits = Student.calc_grade_credits(self)
        i = 0
        print("subject\t\tMarks\t\tGrade\t\tCredits\t\tGrade*Credits")
        for sub, mark in self.__marks.items():
            print(f" {sub}\t\t {mark}\t\t {grade_credits[i]//credit[i]}\t\t {credit[i]}\t\t {grade_credits[i]}")
            i += 1
        print(f"\t\t\t\t\t  Total: {sum(credit)}\t\t {sum(grade_credits)}")

class Generate_Report:
    student_list = []
    @classmethod
    def add_student(cls):
        name = input("Enter student name: ")
        usn = input("Enter student usn: ")
        branch = input("Enter student branch: ")
        sem = input("Enter student semester: ")
        year = input("Enter student year: ")
        s = Student(name,usn,branch,sem,year)
        cls.student_list.append(s)
        print("Student added successfully.")
    
    @classmethod
    def add_marks(cls):
        usn = input("Enter student usn: ")
        for student in cls.student_list:
            if usn == student.get_usn():
                student.add_marks()
                break
        else:
            print("Student Not found.")

    @classmethod
    def generate_report_card(cls):
        usn = input("Enter student usn: ")
        for student in cls.student_list:
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
                print(f"SGPA: {student.calc_sgpa()}")
                print(f"Result: {student.is_passed()}")
                print("--------------------------")
                break
        else:
            print("Student not found.")


def menu():
    print("--- Madan Gowda University, Shivamogga ---")
    print("1. Add Student")
    print("2. Get Report card")
    print("3. Add Marks")
    print("4. Exit")

teacher = Generate_Report()
while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1: teacher.add_student()
    elif choice == 2: teacher.generate_report_card()
    elif choice == 3: teacher.add_marks()
    elif choice == 4: break
    else:
        print("Oh no! Invalid choice, Please enter a valid choice.")
# s = Student("madan",108,"cse",5,3)
# s.add_marks()
# s.display_marks()
# print(s.calc_sgpa())
# print(s.calc_percentage())
