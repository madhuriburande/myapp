## Example: Create a Constructor in Python
class Employee:
    def __init__(self,name,salary):
        print('Inside Constructor')
        self.name=name
        self.salary=salary
    def show(self):
        print("Name:",self.name,"\nSalary:",self.salary)

obj=Employee("Madhuri",100000)
obj.show()

## Default Constructor
class Employee:
    def display(self):
        print("It is default constructor .Python developer")
s1=Employee()
s1.display()
print()

## Non-Parametrized Constructor
class Company:
    def __init__(self):
        self.name="TCS company"
        self.emp_name="Madhuri"
        self.address="pune"
        self.salary=100000
    def show(self):
        print("Compnay Name:",self.name,"\nEmployee Name:",self.emp_name,"\nAddress of Company:",self.address,"\nSalary of emp:",self.salary) 
    
obj=Company()
obj.show()

## Parameterized Constructor
class Employee:
    def __init__(self,name,age,salalry):
        self.name=name
        self.age=age
        self.salary=salalry

    def show(self):
        print("Name:",self.name,"Age:",self.age,"Salary:",self.salary)
con=Employee("Madhuri",26,150000)
con.show()

obj=Employee("Aanat",30,200000)
obj.show()

## Constructor With Default Values
class Student:
    def __init__(self,name,roll_num=7,std=10):
        self.name=name
        self.roll_num=roll_num
        self.std=std

    def display(self):
        print(self.name,self.roll_num,self.std)
a1=Student("komal")
a1.display()

## Constructor Overloading
## At the time of object creation, the interpreter executed the 
# second constructor because Python always considers the last constructor.
## in python overloading method not use becouse python assess the latetest one in that 
# 1one argument,2nd one argumentand third in two arguments if ww  comment 1 and 2only third then it will gives the output.
class Fruits:
    def __init__(self):
        pass

    def abc(self,name):
        self.name=name
        print("Name:",self.name)
    def abc(self,name,color):
        self.name=name
        self.color=color
        print("Name:",self.name,"Color:",self.color)
obj=Fruits()
#obj.abc()
#obj.abc("Apple")
obj.abc("strwberry","Red") 
print()

## Constructor Chaining
class Vehicle:
    def __init__(self,engine):
        print("Inside a Vehicle constructor.")
        self.engine=engine

class Car(Vehicle):
    def __init__(self,engine,max_speed)  :
        super().__init__(engine)  
        print("Inside a car constructor.")
        self.max_sped=max_speed

class Electric_Car(Car):
    def __init__(self,engine,max_speed,km_range):
        print("Inside a Electric_car.")
        super().__init__(engine,max_speed)
        self.km_range=km_range

    def show(self):
        print("Engine:",self.engine,"Max_speed:",self.max_sped,"KM_range:",self.km_range)

obj=Electric_Car('15000cc',240,270)
obj.show()
print()

## Counting the Number of objects of a Class
class employee:
    count=0
    def __init__(self):
        employee.count+=1
e1=employee()
e2=employee()
e3=employee()
print("Employee count:",employee.count)

## Create Destructor using the __del__() Method

class Student:
    def __init__(self,name):
        print("Inside a constructor")
        self.name=name
        print("Object initilized")

    def show(self):
        print("Hello my name is ",self.name)
    
    ## delete destuructor use.
    def __del__(self):
        print("Inside destructor.")
        print("object destructor")

s1=Student("Emma")
s1.show()

del s1
print("delete destructor")




