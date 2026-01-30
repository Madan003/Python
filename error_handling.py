try:
    age = int(input("Enter your age: "))
    print(f"In {100-age} years you will reach 100 years!!!")
except ValueError:
    print("Please enter a valid age!!!")

#value error and division by zero error handling
try:
    a = int(input("Enter frist number: "))
    b = int(input("Enter second number: "))
    print(f"Result: {a/b}")
except ZeroDivisionError:
    print("Divison by zero is not possible, please give a number greater than zero")
except ValueError:
    print("Please enter a valid number!!!")
finally:
    print("Program ended.")