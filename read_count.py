
with open("friends.txt","r") as file:
    count = 0
    for line in file:
        count += 1
    print(f"It has {count} lines.")