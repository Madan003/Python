import csv
class User:
    def __init__(self, name, acc_no, acc_type, balance=0):
        self.__name = name
        self.__accNo = acc_no
        self.__accType = acc_type
        self.__balance = balance
    
    def get_name(self):
        return self.__name
    
    def get_accNo(self):
        return self.__accNo
    
    def get_balance(self):
        return self.__balance
    
    def get_accType(self):
        return self.__accType

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_details(self):
        print(f"Name: {self.__name}")
        print(f"Acc No: {self.__accNo}")
        print(f"Acc Type: {self.__accType}")
        print(f"Balance: {self.__balance} Rupees")

class Bank:
    user_obj = []

    @classmethod
    def loadFile(cls):
        try:
            with open('madanBank.csv') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                for line in reader:
                    name = line[0]
                    acc_no = int(line[1])
                    acc_type = line[2]
                    balance = int(line[3])
                    u = User(name, acc_no, acc_type, balance)
                    cls.user_obj.append(u)
        except FileNotFoundError:
            print("Error!, File not exit, unable to load")

    @classmethod
    def saveFile(cls):
        field_names = ["name","acc_no","acc_type","balance"]
        with open('madanBank.csv','w', newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(field_names)
            for user in cls.user_obj:
                writer.writerow([user.get_name(), user.get_accNo(), user.get_accType(), user.get_balance()])
        print("Data Exported Successfully.")

    @classmethod
    def addNewUser(cls):
        try:
            name = input("Enter Your Name: ")
            acc_no = len(cls.user_obj) + 1001
            acc_type = input("Enter Your Account Type( Savings/Current ): ")
            u = User(name, acc_no, acc_type)
            cls.user_obj.append(u)
            print("Your Account Created Successfully.")
            print("Your Account details: ")
            u.show_details()
        except ValueError:
            print("Error!, Please Enter Correct Details.")
    
    @classmethod
    def deposit(cls):
        try:
            acc_no = int(input("Enter Your Account Number: "))
            for user in cls.user_obj:
                if user.get_accNo() == acc_no:
                    amount = int(input("Enter the amount to deposit: "))
                    user.deposit(amount)
                    print("Amount Deposited to your account successfully.")
                    print(f"Your new Balance is: {user.get_balance()} Rupees")
                    break
            else:
                print("Acoount not found.")
        except ValueError:
            print("Error!, Please Enter Correct Details.")
    
    @classmethod
    def withdraw(cls):
        try:
            acc_no = int(input("Enter Your Account Number: "))
            for user in cls.user_obj:
                if user.get_accNo() == acc_no:
                    amount = int(input("Enter the amount to withdraw: "))
                    if amount <= user.get_balance():
                        user.withdraw(amount)
                        print("Amount Debited Successfully.")
                        print(f"Your new Balance is: {user.get_balance()} Rupees")
                        break
                    else:
                        print("Insufficient Balance..!")
                        break
            else:    
                print("Acoount not found.")
        except ValueError:
            print("Error!, Please Enter Correct Details.")
    
    @classmethod
    def check_balance(cls):
        try:
            acc_no = int(input("Enter Your Account Number: "))
            for user in cls.user_obj:
                if user.get_accNo() == acc_no:
                    print(f"Balance: {user.get_balance()} Rupees")
                    break
            else:
                print("Account Not found.")
        except ValueError:
            print("Error!, Please Enter Correct Details.")

    @classmethod
    def view_all_users(cls):
        if len(cls.user_obj) != 0:
            print(f"Name\tAcc_no\tAcc_type\tBalance")
            for user in cls.user_obj:
                print(f"{user.get_name()}\t{user.get_accNo()}\t{user.get_accType()}\t\t{user.get_balance()}")
        else:
            print("Users list is empty.")

def menu():
    print("-----Madan Bank Of India-----")
    print("1. Create Account\n2. Withdraw\n3. Deposit\n4. Check Balance\n5. View All Users\n6. Export data\n7. Exit")
b = Bank()
b.loadFile()
while True:
    menu()
    try:
        operation = int(input("Enter the option to perform(1-5): "))
        if operation == 1: b.addNewUser()
        elif operation == 2: b.withdraw()
        elif operation == 3: b.deposit()
        elif operation == 4: b.check_balance()
        elif operation == 5: b.view_all_users()
        elif operation == 6: b.saveFile()
        elif operation == 7:
            print("Thank You..!, Madan Bank Of India") 
            break
        else: print("Invalid choice..!")
    except ValueError:
            print("Error!, Please Enter Correct Details.")