from currency_converter import CurrencyConverter
from datetime import date

c = CurrencyConverter()

amount = float(input("Enter the amount in USD: "))

inr = c.convert(amount, 'USD', 'INR', date=date(2015, 9, 29))

print(f"The amount in inr: {round(inr,2)}")