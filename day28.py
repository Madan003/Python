# task 1

temperatures = list(map(int, input("Enter the temperatures: ").split()))

f = list(map(lambda x: (x * 9/5)+32, temperatures))

print(f"Temperatures in Fehrenheit: {f}")

# task 2

cities = ["Bengaluru", "Mysuru", "Mandya", "Hubballi", "Ballari", "Hassan"]

c = list(filter(lambda x: x[0].lower() == 'm', cities))

print(f"The City names starting with 'M': {c}")

# task 3
from functools import reduce

scores = [45, 67, 89, 34, 76, 90]

s = reduce(lambda a,b: a if a > b else b, scores)

print(f'Highest score: {s}')

# task 4

marks = [35, 50, 66, 20, 88, 75]

bonus = list(map(lambda x: x + 10, marks))

passed = list(filter(lambda x: x >= 50, bonus))

total = reduce(lambda a,b: a + b, passed)

print(f"Updated marks: {bonus}")
print(f"Passed marks: {passed}")
print(f"Total marks: {total}")