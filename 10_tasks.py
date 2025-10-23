from functools import reduce

salaries = list(map(int, input("Enter the list of employee salaries: ").split()))

increase = list(map(lambda n:n+(10/100*n),salaries))

extract = list(filter(lambda n:n>50000, increase))

total_payout = round(reduce(lambda a,b:a+b , increase),2)

print(f"The salary list of the employes: {salaries}")
print(f"The salary list of the employes after 10% increase: {increase}")
print(f"The salary list of the employes who's salary is greater than 50,000: {extract}")
print(f"The total payout salary for the employes: {total_payout}")