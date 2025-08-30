while True:
    
    operator = input("Enter operator (+, -, *, /, %, **, //) or type 'exit' to exit:  ")

    if operator.lower() == "exit" :
        print("Calculator is closed, Bye.")
        break

    a = int(input("Enter 1st number: "))
    b= int(input("Enter 2nd number: "))



    if operator == "+":
        result = a + b
        print(f"Result: {result}")
    elif operator == "-":
        result = a - b
        print(f"Result: {result}")
    elif operator == "*":
        result = a * b
        print(f"Result: {result}")
    elif operator == "/":
        if b!=0 :
            result = a / b
            print(f"Result: {result}")
        else :
            print("Error! Division by zero is not possible.")
    elif operator == "%":
        result = a % b
        print(f"Result: {result}")
    elif operator == "**":
        result = a ** b
        print(f"Result: {result}")
    elif operator == "//":
        result = a // b
        print(f"Result: {result}")
    else :
        print("Error! , Invalid operator")