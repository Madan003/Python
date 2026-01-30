print("Enter your 3 friends names: ")

# with is a keyword used in filehandling, it opens respected file and automatically closes it
with open("friends.txt","w") as file:
    for i in range(3):
        name = input("Name: ")
        file.write(f"{name}\n")
