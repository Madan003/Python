import random

random_number = random.randint(1,100)
attempts = 0
while True:
    number = int(input("Guess the number: "))
    if number==random_number:
        print("Correct 🎉, You nailed it.")
        attempts+=1
        break
    elif number>random_number:
        print("Too High! 🚀")
        attempts+=1
    elif number<random_number:
        print("Too Low! ⬇️")
        attempts+=1
print(f"Number of attempts: {attempts}")