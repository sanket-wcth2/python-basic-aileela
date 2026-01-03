class Employee:    #classname
    name = "John" 
    age = 26

emp = Employee()   #obj
print(type(emp))   #check obj type

print(emp.name)    
print(emp.age)

#init

class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.age = int(input("Enter student age: "))

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

stud = Student() #obj
stud.display() #calls obj
