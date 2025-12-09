class User:
    def __init__(self, name, acc_no, acc_type, balance=0):
        self.__name = name
        self.__accNo = acc_no
        self.__accType = acc_type
        self.__balance = balance
    
    def get_accNo(self):
        return self.__accNo
    
    def get_balance(self):
        return self.__balance

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
    user_list = []

    @classmethod
    def addNewUser(cls):
        name = input("Enter Your Name: ")
        acc_no = len(cls.user_list) + 1001
        acc_type = input("Enter Your Account Type( Savings/Current ): ")
        u = User(name, acc_no, acc_type)
        cls.user_list.append(u)
        print("Your Account Created Successfully.")
        print("Your Account details: ")
        u.show_details()
    
    @classmethod
    def deposit(cls):
        acc_no = int(input("Enter Your Account Number: "))
        for user in cls.user_list:
            if user.get_accNo() == acc_no:
                amount = int(input("Enter the amount to deposit: "))
                user.deposit(amount)
                print("Amount Deposited to your account successfully.")
                print(f"Your new Balance is: {user.get_balance()} Rupees")
                break
        else:
            print("Acoount not found.")
    
    @classmethod
    def withdraw(cls):
        acc_no = int(input("Enter Your Account Number: "))
        for user in cls.user_list:
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
    
    @classmethod
    def check_balance(cls):
        acc_no = int(input("Enter Your Account Number: "))
        for user in cls.user_list:
            if user.get_accNo() == acc_no:
                print(f"Balance: {user.get_balance()} Rupees")
                break
        else:
            print("Account Not found.")

def menu():
    print("-----Madan Bank Of India-----")
    print("1. Create Account\n2. Withdraw\n3. Deposit\n4. Check Balance\n5. Exit")
b = Bank()
while True:
    menu()
    operation = int(input("Enter the option to perform(1-5): "))
    if operation == 1: b.addNewUser()
    elif operation == 2: b.withdraw()
    elif operation == 3: b.deposit()
    elif operation == 4: b.check_balance()
    elif operation == 5:
        print("Thank You..!, Madan Bank Of India") 
        break
    else: print("Invalid choice..!")