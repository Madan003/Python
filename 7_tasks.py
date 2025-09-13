#task 2
"""
n = int(input("Enter a number: "))
i = 1
while i<=n:
    while i%2==0:
        i+=1
        continue
    if i<=n:
        print(i)
    i+=1
"""
#task 3 = bus ticket booking

tickets_avl = 8
while tickets_avl>0:
    print(f"{tickets_avl} tickets are available.")
    ticket = input("Do you want bus ticket ( yes or no ): ").lower()

    if ticket == "yes":
        print("Your ticket is booked, happy journey.")
        tickets_avl-=1
    else:
        print("Ok, Thank You!")
        break
if tickets_avl == 0:
    print("Tickets are empty , no more bookings")

# countdown from 10 to 1
i = 10
while i>=0:
    print(i)
    i-=1
print("Happy New Year!")
