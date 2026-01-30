word = input("Enter the word: ")
vowels = ("a","e","i","o","u")
v_count = 0
c_count = 0
for letter in word:
    if letter != " ":
        if letter in vowels:
            v_count += 1
        else:
            c_count += 1
print(f"Vowels count: {v_count}\nConsonants count: {c_count}")