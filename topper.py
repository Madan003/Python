students = {"madan": 93, "shankru": 85 ,"kiran":93,"sheetha": 75}
highest = 0
for mark in students.values():
    if mark>highest:
        highest = mark
for student,mark in students.items():
    if mark == highest:
        print(f"Topper is: {student} - {mark}")