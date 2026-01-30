print("Enter student name and his/her total percentage: ")

with open("marks.txt","w") as file:
    name = input("Name: ")
    percentage = float(input("Percentage: "))
    file.write("Name - Percentage\n")
    file.write(f"{name} - {percentage}%")