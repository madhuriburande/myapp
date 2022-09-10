# create instance variable.
class Student:
    # constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

# create first bject  
print("First object of class")
s1=Student("Jessa",20)
print("Student Name:",s1.name)  
print("Student Age:",s1.age)
print()
# second object
print("second object")
s2=Student("Kelly",21)
print("Student Name:",s2.name)  
print("Student Age:",s2.age)
print()

## Modify Values of Instance Variables
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj=Student("Jessa",20)
print("Name:",obj.name,"Age:",obj.age)

print("here we can see modify or change  instance of variable.")

stud=Student("Madhuri",26)
print("Name:",stud.name,"Age:",stud.age)
print()

## Ways to Access Instance Variable.There are two ways to access the instance variable of class:
# 1.Access instance variable in the instance method

class Student:
# constructoe
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    # instance method access instance variable
    def show(self):
        print("Name:",self.name,"Age:",self.age)

s1=Student("Madhuri",20)
s1.show()
print()

## Access instance variable using getattr()
class Student:
# constructoe
    def __init__(self,name,age):
        self.name=name
        self.age=age

stud=Student("Madhuri",20)
# Use getattr instead of stud.name
print('Name:', getattr(stud, 'name'))
print('Age:', getattr(stud, 'age'))

## Dynamically Add Instance Variable to a Object
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s2=Student("Anant",25)
print("Before add")
print("Name:",s2.name,"Age:",s2.age)
print()

print("after add ")
s2.marks=90
print("Name:",s2.name,"Age:",s2.age,"Marks:",s2.marks)
print()

## Dynamically Delete Instance Variable
class Student:
    def __init__(self,name,roll_num):
        self.name=name
        self.roll_num=roll_num

s2=Student("Anant",28)
print("Name:",s2.name,"Roll_num",s2.roll_num)
print()

# Note---- When we try to access the deleted attribute, it raises an attribute error.
del s2.name
#print(s2.name)

## Access Instance Variable From Another Class
class Vehichle:
    def __init__(self):
        self.engine='1500cc'

class Car(Vehichle):
    def __init__(self,max_speed):
        super().__init__()
        self.max_speed=max_speed
    def display(self):
        print("Engine:",self.engine)
        print("Max speed:",self.max_speed)
obj=Car(200)
obj.display()

## List all Instance Variables of a Object

class Student:
    def __init__(self,roll_num,name):
        self.roll_num=roll_num
        self.name=name
s1=Student("Madhuri",31)
print("Instance varible object has")
print(s1.__dict__)

for key_value in s1.__dict__.items():
    print(key_value[0] ,"=",key_value[1])

class Coffee:
    def __init__(self,hot,cold,cafechinu):
        self.hot=hot
        print("I have one",self.hot,"coffe")
        self.cold=cold
        print("I like",self.cold,"coffe")
        self.cafechinu=cafechinu
        print("And also like",self.cafechinu)
obj=Coffee("hot","cold","cfechinu")
print("Instance varible object has")
print(obj.__dict__)







