def calculatePercentage(marks):
    return round((sum(marks)/600)*100, 2)

def getGrade(percentage):
    if percentage > 90: return "A+"
    elif percentage > 80: return "A"
    elif percentage > 70: return "B+"
    elif percentage > 60: return "B"
    elif percentage > 50: return "C+"
    elif percentage > 40: return "C"
    else: return "Just pass!"

def is_passed(marks):
    is_passed = all(mark>=35 for mark in marks)
    if is_passed:
        return "Pass"
    else:
        return "Fail"