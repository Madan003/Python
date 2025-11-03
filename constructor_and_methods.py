#static method
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

cal = Calculator()
cal.add(4,9)

#bankaccount
class BankAccount:
    bank_name = "Devru Bank"
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited Amount: {amount} and New Balance: {self.balance}")
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"Withdrawed Amount: {amount} and New Balance: {self.balance}")
        else:
            print("Insufficient Balance")
        
    def display(self):
        print(f"Bank Name: {BankAccount.bank_name}")
        print(f"Account Holder: {self.account_holder}\nBalance: {int(self.balance)}")

    @classmethod
    def change_bankname(cls, bank_name):
        cls.bank_name = bank_name
        print(f"New bank name: {bank_name}")
    

acc1 = BankAccount("Devru",99999)
acc1.display()
acc1.change_bankname("Madan Bank")
acc1.deposit(5000)
acc1.withdraw(10000)