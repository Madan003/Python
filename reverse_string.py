num = input("Enter the word: ")
i = len(num) - 1
reversed_num = ""
for n in range(len(num)):
    reversed_num += num[i]
    i -= 1
print(f"Reversed word: {reversed_num}")