
def count_char(s):
    count={}
    for chr in s:
        if chr=='' or chr=='\t':
            continue
        elif chr in count:
            count[chr]+=1
        else:
            count[chr]=1
    for a,b in count.items():
        print("char {} occurence {} times".format(a,b))
s="Madhuri"
count_char(s)

str2="Python"
print(str2)
output=' '
for i in str2:
    output=i+output
print(output)

list2=[11,4,2,6,9,14,31,22]
print(list2)
for i in range(1,len(list2)):
    for j in range(i+1,len(list2)):
        if list2[j]>list2[i]:
            list2[i],list2[j]=list2[j],list2[i]

print(list2)

