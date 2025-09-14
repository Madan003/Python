# task 2

gadgets = {"laptop":60000,"phone":30000,"watch":2300,"mouse":800,"keyboard":600}
total_price = 0
for item,price in gadgets.items():
    total_price+=price
print(total_price)

# task 4

students = [{"name":"madan","age":20,"marks":85},{"name":"harshu","age":18,"marks":95},{"name":"rohith","age":16,"marks":98}]

for student in students:
    print(student)

#task 5
karnataka_cities = {"benaluru":20000000,"shivamogga":500000,"bdvt":200000}

population = {key:values for key,values in karnataka_cities.items() if values<1000000}

print(population)

# task 6
