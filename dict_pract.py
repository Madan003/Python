students = {}
averageMarks = {}
def addStudent():
    name = input("Enter student name: ")
    marks = []
    for i in range(1,7):
        mark = int(input(f"Enter the marks of subject {i}: "))
        marks.append(mark)
    students[name] = marks

def calculateAverageMarks():
    for name,marks in students.items():
        averageMarks[name] = sum(marks)//len(marks)
        print("Average Calculated Successfully.")

def studentWithHighAvg():
    name = ""
    highAverage = 0
    for name, marks in students.items():
        average = sum(marks)//len(marks)
        if average > highAverage:
            highAverage = average
            name = name
    print(f"The student {name} has highest average of: {highAverage}")

def studentWithLowAvg():
    name1 = ""
    lowAverage = 100
    for name, marks in students.items():
        average = sum(marks)//len(marks)
        if average < lowAverage:
            lowAverage = average
            name = name
    print(f"The student {name1} has lowest average of: {lowAverage}")

def menu():
    print("1. Add student")
    print("2. Caculate Average")
    print("3. Student with highest average")
    print("4. Student with lowest average")
    print("5. Exit")
while True:

    choice = int(input("Enter your choice: "))
    if choice == 1: addStudent()
    elif choice == 2: calculateAverageMarks()
    elif choice == 3: studentWithHighAvg()
    elif choice == 4: studentWithLowAvg()
    elif choice == 5: break