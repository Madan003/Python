def inputs():
    kan = int(input("Enter the marks of kan: "))
    eng = int(input("Enter the marks of eng: "))
    maths = int(input("Enter the marks of maths: "))
    phy = int(input("Enter the marks of phy: "))
    bio = int(input("Enter the marks of bio: "))
    return [kan,eng,maths,phy,bio]

def total(marks):
    total_marks = sum(marks)
    per = total_marks/len(marks)
    return [total_marks,per]

def grades(totals):
    per = totals[1]
    if per>=90:
        return "A"
    elif 75 <= per <= 89:
        return "B"
    elif 50 <= per <= 74:
        return "C"
    elif 35 <= per <= 49:
        return "D"
    elif per < 35:
        return "F"

def summary(marks,totals,grade):
    print("*** Student summary of the year 2025 ***")
    for i,sub in enumerate(["Kannada","English","Maths","Physics","Biology"]):
        print(f"{sub}: {marks[i]}")
    print(f"Total marks: {totals[0]}")
    print(f"Percentage is: {totals[1]:.2f}%")
    print(f"Grade: {grade}")

marks = inputs()
totals = total(marks)
grade = grades(totals)
summary(marks,totals,grade)