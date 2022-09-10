import json
fp1=open("Data1.json",'r')
Dict=json.load(fp1)
print(type(Dict))
print("convert json to dictionary=",Dict)

file1=open("data3.json",'r')
d3=json.load(file1)
print("json file to dict=",d3)



file5=open('date4.json','r')

print("Check type",type(json.load(file5)))
