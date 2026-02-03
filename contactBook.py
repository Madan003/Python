class Contacts:
    __contacts = {}
    
    @classmethod
    def addContact(cls):
        try:
            name = input("Enter name: ")
            phoneNo = int(input("Enter Phone Number: "))
            if len(str(phoneNo)) != 10:
                raise Exception("An Indian Phone Number should be 10 digits!!")
            if name not in cls.__contacts:
                cls.__contacts[name] = phoneNo
                print("Contact Added Successfully.")
            else:
                print("Contact with this name already exist!")
        except ValueError:
            print("Please Enter Correct Details!")
        except Exception as e:
            print(f"Error!, {e}")
    
    @classmethod
    def deleteContact(cls):
        try:
            name = input("Enter name of the contact to delete: ")
            cls.__contacts.pop(name)
            print("Contact Deleted Successfully.")
        except KeyError:
            print("Contact name not exit!!")

    @classmethod
    def updateContact(cls):
        try:
            name = input("Enter the name of the contact you want to update: ")
            if name in cls.__contacts:
                number = int(input("Enter the updated phone number: "))
                if len(str(number)) != 10:
                    raise Exception("An Indian Phone Number should be 10 digits!!")
                cls.__contacts[name] = number
                print("Contact updated successfully.")
            else:
                print("Contact not exit!!")
        except ValueError:
            print("Please enter a suitable values!!")
        except Exception as e:
            print(f"Error!, {e}")
    
    @classmethod
    def displayContacts(cls):
        if len(cls.__contacts) != 0:
            print(" Name\t - \tPhone Num")
            for name, number in cls.__contacts.items():
                print(f" {name}\t - \t{number}")
        else:
            print("Contact List is Empty.")

    @classmethod
    def searchContact(cls):
        try:
            name = input("Enter the name of the contact: ")
            if name in cls.__contacts:
                print(f"{name} - {cls.__contacts[name]}")
            else:
                print("Contact not exit!!")
        except ValueError:
            print("Please enter a suitable values!!")
        
def menu():
    print("----- Contacts Book -----")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. View Contacts")
    print("6. Exit")
c = Contacts()
while True:
    menu()
    try:
        choice = int(input("Enter Your Choice: "))
        if choice == 1: c.addContact()
        elif choice == 2: c.deleteContact()
        elif choice == 3: c.updateContact()
        elif choice == 4: c.searchContact()
        elif choice == 5: c.displayContacts()
        elif choice == 6: 
            print("Thank You!")
            break
        else: print("Invalid choice!!!")
    except ValueError:
        print("Enter correct choice!!")