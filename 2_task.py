name = input("Enter your Name :")
age = int(input("Enter your age :"))
height = float(input("Enter your Height(in feet):"))
is_student = input("Are you a student (Enter yes or no):")
if is_student.lower() == "yes":
    is_student = True
elif is_student.lower() == "no":
    is_student = False
else:
    print("Invalid input, only enter yes or no")
    is_student = None

lang = input("Enter your favorite programming language :")
print(f"Hello {name}, you are {age} years old, your height is {height}feet, Student : {is_student}, Favorite language :{lang}")
