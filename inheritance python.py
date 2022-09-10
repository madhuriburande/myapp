## 1.Single Inheritance
## parent class
from unicodedata import name


class Vehicle:
    def vehicale_info(self):
        print("Inside Vehicle class")

## child class
class Car(Vehicle):
    def car_info(self):
        print("Inside car class")

car=Car()
car.vehicale_info()
car.car_info()   
print()  

## Multiple Inheritance-- two parent class and one child class
class Person:
    def person_info(self,name,age):
        print("Inside Person class")
        print("Name:",name,"Age:",age)

class Company:
    def company_info(self,company_name,location):
        print("Inside a company class")
        print("Company_Name:",company_name,"Location:",location)

class Employee(Person,Company):
    def employee_info(self,salary,skill):
        print("Inside a employee class")
        print("Salary:",salary,"Skill:",skill)

emp=Employee()

emp.person_info("Madhuri",26)
print()
emp.company_info("TCS","Pune")
print()
emp.employee_info(100000,"Python Fullstack Developer")
print()

## Multilevel inheritance ---one parent class and two child class.
class Vehicle:
    def car_info(self,name,speed):
        print("Inside a vehicle classs(parent)")
        print("Name:",name,"Speed:",speed)

class Car(Vehicle):
    def sports_car(self,max_distance,speed):
        print("Inside a car class(child)") 
        print("Max_distance:",max_distance,"Speed",speed)

class Bike(Car):
    def bike_info(self,name,price):
        print("Inside a Bike class(child)")
        print("Name:",name,"Price:",price)

b=Bike()
b.car_info("BMW",250)
print()
b.sports_car(270,350)
print()
b.bike_info("R15",150000)
print()

## Hierarchical Inheritance--one parent class and two chils class but inchild use parent below example
class Cookies:
    def chocolate(self,name,contity):
        print("Inside a cookies class")
        print("Name:",name,"Contity",contity)
class cake(Cookies):
    def muffine(self,name,price):
        print("Inside a cake class")
        print("Name:",name,"Price:",price)
class Brad(Cookies):
    def bun_brad(self,name,color):
        print("Inside Brad class")
        print("Name:",name,"Color:",color)


b=cake()
b.chocolate("Coffe",10)
b.muffine("Venila",100)
print()
c=Brad()
c.bun_brad("Sandwich Brad","Brown")
c.chocolate("strwberry",50)
print()

## Hybrid Inheritance
class Fruits:
    def fruits_info(self,name,color):
        print("Inside a fruits class(parent)")
        print("Name:",name,"Color:",color)

class Snack(Fruits):
    def snack_info(self,name,contity):
        print("Inside a snackclass(child)")
        print("Name:",name,"contity:",contity)

class pizza(Fruits):
    def pizza_info(self):
        print("Inside Pizza class")

class sandwich(Snack,Fruits):
    def sandwich_info(self):
        print("Inside a sandwich class")
s=sandwich()
s.fruits_info("Apple","Red")
s.snack_info("Samosa",10)
s.sandwich_info() 
print()                   

### Python super() function------###

class Employee:
    def __init__(self):
        pass
    def show(self):
        print("i am parent class")
class Company(Employee):
    def show(self):
        super().show()
        print("I am child class")

obj=Company()
obj.show() 
print()       

class Person:
    def __init__(self,name,last_name) :
        self.name=name
        self.last_name=last_name
    def display(self):
        print("I am parent class")
        print("Name:",self.name,"last_name:",self.last_name)    
class details(Person): 
    def display(self):
        
        print("I am child class")  
        super().__init__() 


obj=Person("Madhuri","Burande")
obj.display() 

## Method Resolution Order(MRO)
class A:
    def add(sel,a,b):
        print("Addition of a and b is:",a+b)
class B(A):
    def sub(self,x,y):
        print("subtraction of x and y is:",x-y)
class C(B,A):
    def div(self,p,q):
        print("Divisition of p  and q is:",p/q)

arithmetic=C()
arithmetic.add(10,5)
arithmetic.sub(20,10)
arithmetic.div(45,5)
print(C.mro())

     




