# task 1
def logger(func):
    def wrapper(a, b):
        print(f"Function '{func.__name__} is called.")
        return func(a, b)
    return wrapper


@logger
def multiply(a,b):
    return a * b

@logger
def division(a,b):
    return a / b

print(division(100, 8))

# task 2
import datetime


def timer(func):
    def wrapper():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(f"Time taken to execute '{func.__name__}' function: {(end_time - start_time).total_seconds()}sec")
    return wrapper

@timer
def sumneOnduFunction():
    for i in range(10):
        print("Bsdk")

sumneOnduFunction()

# task 3
def sumne1(func):
    def wrapper(name):
        print("===")
        func(name)
        print("===")
    return wrapper

def sumne2(func):
    def wrapper(name):
        print(">>>")
        func(name)
    return wrapper

@sumne1
@sumne2
def printMyName(name):
    print(f"My name is: {name}")

printMyName("Madan Gowda")

# task 4
def view_name(func):
    def wrapper(name):
        if name == "admin":
            print("Access Granted.")
        else:
            print("Access Denied!")
    return wrapper

@view_name
def request_access(name):
    pass

request_access("admin")