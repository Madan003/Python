# tables 


for j in range(2,11):
    for i in range(1,11):
        product = j * i
        print(f"{j} * {i} = {product}")

laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya","madan","pruthvi"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")


# multiples

for i in range(1,31):
    if i%3==0:
        print(i,end=" ")
print()
    
# sum of 10 numbers
x = 0
for i in range(1,11):
    x += i
print(x)


# printing letter in name

a = input("Enter a name: ")
for letter in a:
    print(letter,end=" ")
print()

#count vowels in string

string = input("Enter a string: ")
vowels = 0
for letter in string:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels += 1
print(f"Number of vowels are: {vowels}")