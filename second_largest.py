print("Enter the marks of 6 subjects: ")
marks = []
for i in range(6):
    mark = int(input("Marks: "))
    marks.append(mark)
marks.sort(reverse=True)
print(f"Second largest element is: {marks[1]}")