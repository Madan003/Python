from mylibrary import student_utils as student

marks = [int(mark) for mark in input("Enter the 6 subject marks in space separated format: ").split()]

for i, mark in enumerate(marks):
    print(f"Subject {i+1}: {mark}")

percentage = student.calculatePercentage(marks)
grade = student.getGrade(percentage)
result = student.is_passed(marks)

print(f"Total Percentage: {percentage}%")
print(f"Grade: {grade}")
print(f"Result: {result}")