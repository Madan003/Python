n = int(input("Enter a number: "))

#factorial
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

#fibonacci
def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        print(a, end=" ")
        a,b = b, a+b

#sum of digits
def addition(n):
    if n==0:
        return 0
    return (n%10) + addition(n // 10)

print(f"Factorial of {n} is: {fact(n)}")
print(f"Fibonacci sequence of {n} is: ",end="")
fibonacci(n)
print()
print(f"Sum of digits of {n} is: {addition(n)}")