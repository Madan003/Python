class Contacts:
    __contacts = {}
    
    @classmethod
    def addContact(cls):
        try:
            name = input("Enter name: ")
            phoneNo = int(input("Enter Phone Number: "))
            cls.__contacts[name] = phoneNo
            print("Contact Added Successfully.")
        except ValueError:
            print("Please Enter Correct Details!")
    
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
        pass
    
    @classmethod
    def displayContacts(cls):
        if len(cls.__contacts) != 0:
            print(" Name - Phone Num")
            for name, number in cls.__contacts.items():
                print(f"{name} - {number}")
        else:
            print("Contact List is Empty.")
        
def menu():
    print("----- Contacks Book -----")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. View Contacts")
    print("5. Exit")
c = Contacts()
while True:
    menu()
    try:
        choice = int(input("Enter Your Choice: "))
        if choice == 1: c.addContact()
        elif choice == 2: c.deleteContact()
        elif choice == 3: c.updateContact()
        elif choice == 4: c.displayContacts()
        elif choice == 5: 
            print("Thank You!")
            break
    except ValueError:
        print("Enter correct choice!!")