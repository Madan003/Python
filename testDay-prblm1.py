# problem 1

arr = list(map(int, input("Enter the array: ").split()))

arr = set(arr)

arr = list(arr)

arr.sort()

print(f"Maximum: {max(arr)}")
print(f"Minimum: {min(arr)}")
print(f"Average: {sum(arr)//len(arr)}")