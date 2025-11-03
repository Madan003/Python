class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.__acc_no = acc_no
        self.__balance = balance
    
    def check_balance(self):
        print(f"The available balance is : {self.__balance}")

    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited Amount: {amount} and New Balance: {self.__balance}")
    
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            print(f"Withdrawed Amount: {amount} and New Balance: {self.__balance}")
        else:
            print("Insufficient Balance")

acc1 = BankAccount("Devru",108,50000)    
acc1.deposit(15000)
acc1.withdraw(5000)
acc1.check_balance()
print(acc1.__acc_no)
print(acc1.__balance)