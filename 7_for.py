# searching
string = "karnataka"
a = input("Enter a letter to find: ").lower()
for letter in string:
    if letter.lower() == a:
        print("Letter Found.")
        break
else:
    print("Letter not found.")