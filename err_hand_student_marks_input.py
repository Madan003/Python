try:
    print("-------Madan Gowda University, Shivamogga.------")
    SEPM = int(input("Enter the marks of SEPM: "))
    if SEPM < 0 or SEPM>100:
        raise Exception("Marks should be within 0 to 100. Negative or greater than 100 marks are not accepted.")
    CN = int(input("Enter the marks of CN: "))
    if CN < 0 or CN>100:
        raise Exception("Marks should be within 0 to 100. Negative or greater than 100 marks are not accepted.")
    TOC = int(input("Enter the marks of TOC: "))
    if TOC < 0 or TOC>100:
        raise Exception("Marks should be within 0 to 100. Negative or greater than 100 marks are not accepted.")
    RM = int(input("Enter the marks of RM: "))
    if RM < 0 or RM>100:
        raise Exception("Marks should be within 0 to 100. Negative or greater than 100 marks are not accepted.")
    AI = int(input("Enter the marks of AI: "))
    if AI < 0 or AI>100:
        raise Exception("Marks should be within 0 to 100. Negative or greater than 100 marks are not accepted.")
    total_marks = SEPM+CN+TOC+RM+AI
    percentage = round((total_marks/500)*100,2)
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage}")
except ZeroDivisionError:
    print("Division by zero is not possible, please enter a number greater than zero.")
except ValueError:
    print("Enter a valid Number.")
except Exception as e:
    print(e)
finally:
    print("Thank You!")