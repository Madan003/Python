num = input("Enter the number: ")
i = len(num) - 1
reversed_num = ""
for n in range(len(num)):
    reversed_num += num[i]
    i -= 1
if reversed_num == num:
    print("It is Palindrome!")
else:
    print("It is not Palindrome!")