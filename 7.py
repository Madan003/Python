#braek and continue and while

is_failed = True
i = 1

while is_failed :
    if(i%2==0):
        i = i+1
        if i>100:
            break
        continue
    print(f"Attempt {i}.")
    i=i+1
    if(i>100):
        break

#counting n numbers
i = 1
sum = 0
while i<=10:
    sum = sum + i;
    i = i + 1
print(sum)

# print * as a traiangle,right angled triangle , left angled triangle
n = int(input(" Enter a number: "))
i = 1
while i<=n:
    j=n
    y = i
    # if we dont write this block it will become right angled traingle
    while j>y:
        print(" ",end="")
        y+=1
    x=1
    k=1
    while x<=i:
        # if we gave space in end it will become full triangle with inbetween space
        # if we wrote only this block without space in end it will become left angled traingle
        print("*",end="")
        x+=1
        # full traingle without in between space
        while k<i:
            print("*",end="")
            k+=1
    print("")
    i+=1

# atm pin checker with only 3 trails for a day
pin = "0329"
i = 1
while i<=3:
    input_pin = input("Enter your 4 digit pin: ")
    if input_pin == pin:
        print("Correct, Go ahead")
        break
    elif i<3:
        print("Incorrect try again.")
    else:
        print("Tody trials are over please try tomorrow.")
    i+=1