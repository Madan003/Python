products = {}
def addProduct():
    product_id = input("Enter Product id: ")
    product_name = input("Enter Product name: ")
    product_price = float(input("Enter Product prize: "))
    product_quantity = int(input("Enter Product Quantity: "))
    details = {}
    details["name"] = product_name
    details["price"] = product_price
    details["quantity"] = product_quantity
    products[product_id] = details
    print("Product Added Successfully.")

def removeProduct():
    product_id = input("Enter Product id to remove: ")
    if product_id in products:
        products.pop(product_id)
        print("Product Removed Successfully.")
    else:
        print("Product not found!!")

def displayProducts():
    if len(products) > 0:
        for product_id, details in products.items():
            print(f"Product Id: {product_id}")
            for tag, name in details.items():
                print(f"{tag} - {name}")
            print("--------------------------")
    else:
        print("Product list is empty.")

def updateStock():
    product_id = input("Enter product id to update its stock: ")
    for product, details in products.items():
        if product == product_id:
            new_quantity = int(input("Enter its new stock quantity: "))
            details["quantity"] = new_quantity
            print("Product stock updated succesfully.")
            break
    else:
        print("Product not found")
    
def showOutOfStockProducts():
    if len(products) > 0:
        counter = 0
        for product_id, details in products.items():
            if details["quantity"] == 0:
                print(f"Product Id: {product_id}")
                for tag, name in details.items():
                    print(f"{tag} - {name}")
                print("--------------------------")
                counter += 1
        if counter == 0:
            print("All products are in stock.")
    else:
        print("Product list is empty.")

def menu():
    print("1. Add Product\n2. Remove Product\n3. Update Stock\n4. Show out of stock products\n5. Display All Products\n6. Exit")

while True:
    menu()
    choice = int(input("Enter Your Choice: "))
    if choice == 1: addProduct()
    elif choice == 2: removeProduct()
    elif choice == 3: updateStock()
    elif choice == 4: showOutOfStockProducts()
    elif choice == 5: displayProducts()
    elif choice == 6: 
        print("Thank You!!")
        break