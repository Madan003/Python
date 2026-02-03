
name = input("Enter name to search: ")

with open("friends.txt","r") as file:
    for line in file:
        if line.strip() == name: 
            print("Found!")
            break
    else:
        print("Not Found!")