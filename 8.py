def func(num):
    return int(str(num)*3)

a = 100

c = a + func(2)

print(c)

#task 1
def greet():
    print("Hello everyone!")

greet()

#task 2
def greet_user(user="user"):
    print(f"Hello {user}, welcome to our store")

greet_user("madan")

#task 3
def add(a,b):
    return a+b
c=25
c += add(5,7)
print(c)

