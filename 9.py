#factorial using loops
i = int(input("Enter a num: "))
fact = 1
while i>1:
    fact = fact * i
    i -= 1
print(fact)

#lambda functions
mul = lambda a,b: a*b
print(mul(8,6))

#recursion function to calculate sum of first n numbers
def sum_of_n(n):
    if n==1:
        return 1
    return n + sum_of_n(n-1)

print(sum_of_n(10))

#variable length arguments function that returns their average
def average(*n):
    total = 0
    for i in n:
        total+=i
    ave = total/len(n)
    return ave

print(average(1,2,3,4,5,6,7,8,9,10))

#recursion function to add a digits of a number
def addition(n):
    if n==0:
        return 0
    return (n%10) + addition(n // 10)

print(addition(456))