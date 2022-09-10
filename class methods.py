## Example 1: Create Class Method Using @classmethod Decorator
from datetime import date
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def Calculate_age(cls,name,birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year-birth_year)
    def show(self):
        print(self.name,"age is:"+ str(self.age))
abc=Student("Madhuri",26)
abc.show()

xyz=Student.Calculate_age("Anat",1991)
xyz.show()

## same another exmple
class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    
    @classmethod
    def calculate_age(cls,name,birth_year,sex):
        return cls(name,date.today().year-birth_year,sex)
    def display(self):
        print(self.name,"age is:"+str(self.age),self.sex)

obj=Person("Aankita",23,", female")
obj.display()

s1=Person.calculate_age("Komal",2005,", female")
s1.display()

#Example 2: Create Class Method Using classmethod() function
class School:
   name="ABC School"
   def  school_name(cls):
    print("School Name is :",cls.name)
School.school_name=classmethod(School.school_name)
School.school_name()

## Example 3: Access Class Variables in Class Methods
class Student:
    School_name="ABC school"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def Change_school(cls,School_name):
        cls.School_name=School_name

    def show(self):
        print("Name:",self.name,"\nAge:",self.age,"\nSchool Name:",Student.School_name)
    
sony=Student("Harshada",15)
sony.show()

Student.Change_school("XYZ School")
sony.show()

## Class Method in Inheritance
class Vehicle:
    brand_name="BMW"
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @classmethod
    def from_price(cls,name,price):
        return cls(name,(price*75))
    def show(self):
        print(self.name,self.price)

class Car(Vehicle):
    def average(self,distance,fuel_used):
        mileage=distance/fuel_used
        print(self.name,"Mileage :",mileage)

bmw_us=Car("BMW X5",65000)
bmw_us.show()

bmw_ind=Car.from_price("BMW X5",65000)
bmw_ind.show()



