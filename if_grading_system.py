marks = int(input("Enter your marks(0-100): "))

if marks>= 90:
    print("Your Grade is: A")
elif  75<=marks<90:
    print("Your Grade is: B")
elif  50<=marks<75:
    print("Your Grade is: C")
elif  35<=marks<50:
    print("Your Grade is: D")
elif marks<35:
    print("Your Grade is: F")