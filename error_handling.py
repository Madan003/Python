

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