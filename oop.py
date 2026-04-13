class Parrot:
    species='bird'

    def __init__(self,name,age):
        self.name=name
        self.age=age

bluey=Parrot("Bluey",10)


print(bluey.name,'is',bluey.age,"years")


chloe=Parrot("chloe",8)


print(chloe.name,'is',chloe.age,"years")

#code 2
class student:
    stream='coding'

    def __init__(self,roll,adress):
        self.roll=roll
        self.adress=adress

student1=student( 17, "Dhanmondi,Dhaka-1205")

print("Student's roll number is",student1.roll,"Student's adress is",student1.adress)

student2=student(38, "Green Road,Dhaka-1205")

print("Student's roll number is", student2.roll, "Student's adress is",student2.adress)