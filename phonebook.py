import sys
# Create initial phonebook
def initial_phonebook():
    rows,cols=int(input("Please enter initial number of contacts")),5
    phone_book=[]

    for i in range(rows):
        print("\n Enter contact details"%(i+1))
        temp=[]

    for j in range(cols):
        if j==0:
            temp.append(str(input("Enter name:")))
            if temp[j]=="":
                sys.exit("Name is Mandatory!")

        if j==1:
            temp.append(int(input("Enter number:")))

        if j==2:
            temp.append(str(input("Enter email:")))
            if temp[j]=="":
                temp[j]=None
        
         if j==3:
            temp.append(str(input("Enter DOB:")))
            if temp[j]=="":
                temp[j]=None

         if j==4:
            temp.append(str(input("Enter Catagory:")))
            if temp[j]=="":
                temp[j]=None        

    phone_book.append(temp)
    
#Menu
def Menu():
    print("\n 1.ADD")
    print("2.Remove")
    print("3.Delete all")
    print(4.Display All)
    print(5.Exit)
    return int(input("Enter Choice"))





