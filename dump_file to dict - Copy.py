import json
fp=open("Date2.json",'w')
d1={"a":1,"b":2}
print("convert json to file format in dictionary")
res=json.dump(d1,fp)
print(type(d1))

import json
fp1=open("Json_to_Dict_file.json",'w')
d2={ "name": "Kelly","age":25,  "salary": 8000,  "city": "New york" }
z=json.dump(d2,fp1)

file3=open('Json_data_dict.json','w')
d5={
    "name": "Madhuri Burande",
    "salary": 100000,
    "skills": [
        "Python full stack developer",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}

opuput=json.dump(d5,file3)

## by using class

class Person_Info:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name:",self.name,"Age:",self.age)
        
obj=Person_Info("Anant",30)
dict_1={"Location":"Pune","Salary":10000,"Job":"GOV"}
file4=open('new_jtod.json','w')
res1=json.dump(dict_1,file4)
        