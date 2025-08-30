#task 2
age = int(input("Enter your age: "))

if age>=18 :
    print("You are adult.")
else :
    print("You are minor.")

#task 3
a = input("Enter your full name: ")

print("a" in a)
print("python" not in a)

#task 4
a = int(input("Enter 1st number: "))
b= int(input("Enter 2nd number: "))

print(a & b)
print(a | b)
print(a ^ b)
print(a<<3)
print(b>>2)