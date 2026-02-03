print("Enter a list of numbers: ")
numbers = [int(number) for number in input().split()]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
unique_numbers = []
duplicate_numbers = []
for number, freq in frequency.items():
    if freq > 1:
        duplicate_numbers.append(number)
    else:
        unique_numbers.append(number)
print(f"Unique numbers: {unique_numbers}")
print(f"Duplicate numbers: {duplicate_numbers}")