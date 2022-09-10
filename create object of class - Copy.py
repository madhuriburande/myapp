class Person:
    def __init__(self,name,age,sex,profession):
        self.name=name
        self.age=age
        self.sex=sex
        self.profession=profession
    def show(self):
        print("Name:",self.name,"\nAge:",self.age,"\nSex:",self.sex,"\nProfession:",self.profession)

    def work(self):
        print("Hi i am ",self.name,"and i am softeware engineering.")

obj=Person("Madhuri",26,"Female","Python dev")
obj.show()
obj.work()

## Accessing properties and assigning values
class Student:
    ## class varible
    school_name="ABC school"
    ## constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("Komal",16)
print("Student:",s1.name,"and her age is",s1.age)   

## Asscess class varible
print("School name:",Student.school_name)

## Modyfing instance variable
s1.name="Swara"
s1.age="12"
print("Student:",s1.name,"and her age is",s1.age)

## modify class variable
Student.school_name="XYZ School"
print("School name:",Student.school_name)

## class Method Accessing properties and assigning values

class Person:
    company_name="MNC company"
    def __init__(self,name,age,profesion):
        self.name=name
        self.age=age
        self.profesion=profesion
    def show(self):
        print("Name:",self.name,"\nAge:",self.age,"\nprofesion:",self.profesion)

    def change_age(self,new_age):
        self.age=new_age

    @classmethod
    def modifying_compnay (cls,new_company):
        cls.company_name=new_company

s1=Person("Harry",25,"java Dev.")
s1.show()

s1.change_age(27)
Person.modifying_compnay("TCS compnay")
s1.show()

## Modify Object Properties
class Fruits:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def show(self):
        print("Fruit Name:",self.name,"\nFruit Color:",self.color)

obj=Fruits("Apple","Red")
obj.show()

## modifying name
obj.name="Strawberry"
obj.show()

