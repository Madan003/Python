import json
class ExpenseTracker:
    __data = {}

    @classmethod
    def loadFile(cls):
        try:
            with open("expenses.json",'r') as file:
                cls.__data = json.load(file)
        except FileNotFoundError:
            cls.__data = {
                "Grocery & Home": {
                    "Total": 0.0
                },
                "Clothes, friends & Outing": {
                    "Total": 0.0
                },
                "Personal Spends": {
                    "Total": 0.0
                },
                "Investment": {
                    "Total": 0.0
                },
                "Total": 0.0
            }
            
    @classmethod
    def saveToFile(cls):
        with open("expenses.json", 'w') as file:
            json.dump(cls.__data, file, indent=2)

    @classmethod
    def categories(cls):
        print("*** Categories ***")
        print("1. Grocery & Home.")
        print("2. Clothes, friends & Outing")
        print("3. Personal Spends")
        print("4. Investment")

    @classmethod
    def addExpenses(cls):
        cls.categories()
        category = input("Enter the category of your expense: ")
        date = input("Enter date of spent(format: 'DD-MM-YYYY'): ")
        amount = float(input("Enter the amount: "))
        match category:
            case "1":
                target = cls.__data["Grocery & Home"]
                target[date] = amount
                target["Total"] += amount
            case "2":
                target = cls.__data["Clothes, friends & Outing"]
                target[date] = amount
                target["Total"] += amount
            case "3":
                target = cls.__data["Personal Spends"]
                target[date] = amount
                target["Total"] += amount
            case "4":
                target = cls.__data["Investment"]
                target[date] = amount
                target["Total"] += amount
            case _:
                print("Wrong Choice!, try later.")
        cls.__data["Total"] += amount
        cls.saveToFile()

    @classmethod
    def viewExpensesByCategory(cls):
        for category, target in cls.__data.items():
            if category != "Total":
                amount = target["Total"]
                print(f"Total Expense by {category} is: {amount} Rupees")
                print()

    @classmethod
    def viewTotalExpenses(cls):
        amount = cls.__data["Total"]
        print(f"Total Expense: {amount} Rupees")
    

def menu():
    print("*** Expense Tracker ***")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

e = ExpenseTracker()
e.loadFile()

while True:
    menu()
    choice = int(input("Enter the choice: "))
    match choice:
        case 1: e.addExpenses()
        case 2: e.viewExpensesByCategory()
        case 3: e.viewTotalExpenses()
        case 4: 
            print("Thank You!")
            break
        case _: print("Invalid Choice!")