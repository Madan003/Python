courses = {"kannada":set(),"english":set()}
def addStudent():
    student_id = int(input("Enter student id: "))
    course = input("Enter the course name the student wants to enroll: ")
    for course_name,students in courses.items():
        if course.lower() == course_name.lower():
            students.add(student_id)
            print("Student enrolled successfully.")
            break
    else:
        print("Course not found!!")

def removeStudent():
    cousre = input("Enter course name of the student: ")
    for course_name, students in courses.items():
        if cousre.lower() == course_name.lower():
            student_id = int(input("Enter student id to remove: "))
            if student_id in students:
                students.remove(student_id)
                print("Student removed successfully.")
                break
            else:
                print("This student not enrolled this course!!!")
                break
    else:
        print("Course not found!!!")

def showCommonStudentsInAllCourses():
    course = input("Enter two course names to get common students: ").split()
    if len(course) == 2:
        course1 = course[0]
        course2 = course[1]
        if course1 in courses and course2 in courses:
            common_students = courses[course1].intersection(courses[course2])
            print(common_students)
        else:
            print("Courses not found!!")
    else:
        print("Please enter two course names!!")

def showUniqueStudents():
    course = input("Enter two course names to get unique students: ").split()
    if len(course) == 2:
        course1 = course[0]
        course2 = course[1]
        if course1 in courses and course2 in courses:
            unique_students = courses[course1].difference(courses[course2])
            print(unique_students)
        else:
            print("Courses not found!!")
    else:
        print("Please enter two course names!!")

def menu():
    print("1. Add student\n2. Remove student\n3. Show common students\n4. Show unique students\n5. Exit")

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1: addStudent()
    elif choice == 2: removeStudent()
    elif choice == 3: showCommonStudentsInAllCourses()
    elif choice == 4: showUniqueStudents()
    elif choice == 5:
        print("Thank You!") 
        break