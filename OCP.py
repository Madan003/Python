class BillingSystem:
    def calc_tax(self):
        return 0

class Food(BillingSystem):
    def calc_tax(self):
        return 10
    
class Electronics(BillingSystem):
    def calc_tax(self):
        return 20

f = Food()
e = Electronics()
b = BillingSystem()
print(f.calc_tax())