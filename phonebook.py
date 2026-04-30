import sys
# Create initial phonebook
def initial_phonebook():
    rows,cols=int(input("Please enter initial number of contacts")),5
    phone_book=[]

    for i in range(rows):
        print("\nEnter contact details % " , (i + 1))
        temp = []

        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name: ")))
                if temp[j] == "":
                    sys.exit("Name is Mandatory!")
            elif j == 1:
                temp.append(int(input("Enter number: ")))
            elif j == 2:
                email = input("Enter email: ")
                temp.append(email if email else None)
            elif j == 3:
                dob = input("Enter DOB: ")
                temp.append(dob if dob else None)
            elif j == 4:
                category = input("Enter Category: ")
                temp.append(category if category else None)

    phone_book.append(temp)
    
#Menu
def Menu():
    print("\n 1.ADD")
    print("2.Remove")
    print("3.Delete all")
    print("4.Display All")
    print("5.Exit")
    return int(input("Enter Choice"))

def add(pb):
    temp = []
    print('Enter new contact details')

    temp.append(input("Enter name: "))
    temp.append(int(input("Enter number: ")))

    email = input("Enter email: ")
    temp.append(email if email else None)

    dob = input("Enter DOB: ")
    temp.append(dob if dob else None)

    category = input("Enter category: ")
    temp.append(category if category else None)

    pb.append(temp)
    print("Contact added successfully")
    return pb


def remove(pb, name):
    for contact in pb:
        if contact[0] == name:
            pb.remove(contact)
            print('Contact removed successfully')
            return pb

    print("Contact not found")
    return pb

def display(pb):
    if not pb:
        print("List is empty")
    else:
        for i in range(len(pb)):
            print(pb[i])

print("Welcome to the Phonebook Application")
pb=initial_phonebook()
while True:
    ch=Menu()
    if ch==1:
        pb=add(pb)
    elif ch==2:
        name=input("Enter name to remove: ")
        pb=remove(pb,name)
    elif ch==3:
        pb.clear()
        print("All contacts deleted")
    elif ch==4:
        display(pb)
    elif ch==5:
        print("Good Bye!")
        break




