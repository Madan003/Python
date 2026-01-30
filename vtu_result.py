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
        SEPM = int(input("Enter the marks of Software Engineering & Project Management: "))
        self.__marks["SEPM"] = SEPM
        CN = int(input("Enter the marks of Computer Networks: "))
        self.__marks["CN"] = CN
        TOC = int(input("Enter the marks of Theory of Computation: "))
        self.__marks["TOC"] = TOC
        WEB = int(input("Enter the marks of Web Technology LAB: "))
        self.__marks["WEB"] = WEB
        AI = int(input("Enter the marks of Artificial Intelligence: "))
        self.__marks["AI"] = AI
        MP = int(input("Enter the marks of Mini Project: "))
        self.__marks["MP"] = MP
        EVS = int(input("Enter the marks of Environmental studies and E-waste management: "))
        self.__marks["EVS"] = EVS
        RM = int(input("Enter the marks of Reasearch Methodology: "))
        self.__marks["RM"] = RM
        print("Marks added successfully.")
    
    def calc_percentage(self):
        total_marks = sum(self.__marks.values())
        if len(self.__marks) > 0:
            return round((total_marks/(len(self.__marks)*100))*100,2)
        else:
            return 0
        
    def calc_grade_credits(self):
        # grade * credits of each subject
        credit = [4,4,4,1,3,2,1,3]
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
        total_credits = 22
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
    
    def remarks(self):
        sgpa = Student.calc_sgpa(self)
        if sgpa >= 9:
            return "Excellent bruhh!, Your SGPA is bahut jyadha hai!! in this SGPA two students will pass, please concentrate on skill development."
        elif sgpa >= 8.5:
            return "Very good bruhh!, Your SGPA is enoughhhhhhh bruhhh!!, now concentrate more on skills & placements."
        elif sgpa >= 8:
            return "Very good bruhh!, try to improve your SGPA above 8.5 and concentrate more on placements."
        elif sgpa >= 7.5:
            return "Good bruuuhh!, try to improve your SGPA above 8.5 and concentrate more on placements."
        else:
            return "SGPA is not barrier for placements, but it clears first door so concentrate on both SGPA and placements"
    
    def display_marks(self):
        credit = [4,4,4,1,3,2,1,3]
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
    def calculateSGPA(cls):
        try:
            usn = input("Enter Your USN: ")
            branch = "CSE"
            sem = "5th"
            year = "3rd"
            if usn == "1AY23CS075":
                name = "Gagan bhai"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            elif usn == "1AY23CS087":
                name = "Sheethaaaa"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            elif usn == "1AY23CS088":
                name = "E-leg Hemuu"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            elif usn == "1AY23CS090":
                name = "Sede G1"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            elif usn == "1AY23CS102":
                name = "Kudluuuurrr"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            elif usn == "1AY23CS107":
                name = "Maguuuuu"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            elif usn == "1AY23CS108":
                name = "Madan"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            elif usn == "1AY23CS166":
                name = "Shyyyyy"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            elif usn == "1AY23CS178":
                name = "Bhooothaa"
                s = Student(name,usn,branch,sem,year)
                cls.student_list.append(s)
                print(f"Ohh {name} Welcome!")
                s.add_marks()
                cls.generate_report_card(s)
            else:
                print("Student not found!, please enter correct USN!!!")
        except ValueError:
            print("Error!, Enter correct details.")

    @classmethod
    def generate_report_card(cls, student):
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
        print(f"Remarks: {student.remarks()}")
        print(f"Result: {student.is_passed()}")
        print("--------------------------")

def menu():
    print("--- VTU SGPA Calculator ---")
    print("1. Calculate SGPA")
    print("2. Exit")

teacher = Generate_Report()
while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1: teacher.calculateSGPA()
        elif choice == 2: break
        else:
            print("Oh no! Invalid choice, Please enter a valid choice.")
    except ValueError:
        print("Error!, Enter correct choice!!!")