age = int(input("Enter your age: "))

total_price = 0

popcorn = input("If you want popcorn(yes or no): ")

popcorn_price = 50

if age<5:
    print("Ticket is free.")
    if popcorn.lower() == "yes":
        total_price =total_price + popcorn_price
    elif popcorn.lower() == "no":
        total_price
    else:
        print("Please either yes or no/")

    print("****** Summary ******")
    print(f"Age of the customer: {age}\nTicket type: Free Ticket\nPopcorn: {popcorn}\nFinal price: {total_price} rupees.")
elif 5<=age<18:
    print("Ticket cost is 100.")
    total_price = total_price + 100
    if popcorn.lower() == "yes":
        total_price += popcorn_price
    elif popcorn.lower() == "no":
        total_price
    else:
        print("Please either yes or no/")
    print("****** Summary ******")
    print(f"Age of the customer: {age}\nTicket type: Child Ticket\nPopcorn: {popcorn}\nFinal price: {total_price} rupees.")
elif 18<= age <60:
    print("Ticket cost is 200.")
    total_price = total_price +200
    if popcorn.lower() == "yes":
        total_price += popcorn_price
    elif popcorn.lower() == "no":
        total_price
    else:
        print("Please either yes or no/")
    print("****** Summary ******")
    print(f"Age of the customer: {age}\nTicket type: Adult Ticket\nPopcorn: {popcorn}\nFinal price: {total_price} rupees.")
elif age >= 60:
    print("Ticket cost is 150.")
    total_price = total_price + 150
    if popcorn.lower() == "yes":
        total_price += popcorn_price
    elif popcorn.lower() == "no":
        total_price
    else:
        print("Please either yes or no/")
    print("****** Summary ******")
    print(f"Age of the customer: {age}\nTicket type: Senior citizen Ticket\nPopcorn: {popcorn}\nFinal price: {total_price} rupees.")