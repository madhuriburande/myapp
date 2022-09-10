# que1. Python program to get Current Timeimport time
# import time
# Current_time=time.time()
# print("Time:",Current_time)

#que2. Get Current Date and Time using Python
# from datetime import datetime
# today=datetime.now()
# print("Current Date and Time :",today)

#que3. Python | Find yesterday’s, today’s and tomorrow’s date
# from datetime import date,timedelta
# current_date=date.today()
# print("Todays Date:",current_date)

# yesterday=current_date-timedelta(1)
# print("Yesterday's :",yesterday)

# tomarrow= current_date + timedelta(1)
# print("Tomarrow Date :",tomarrow)


#que4. Python program to convert time from 12 hour to 24 hour format.
# from datetime import datetime
# now = datetime.now()

# current_time=now.time()
# print(current_time.strftime("%I:%M:%S"))

# hrs_24=current_time.strftime("%H:%M:%S")
# print(hrs_24)

#que5. Python program to find difference between current time and given time.

# def time_difference(h1, m1, h2, m2):
#     print("The current times:", h1,":",m1)
#     t1 = h1 * 60 + m1
#     print("The given times:",h2,":",m2)
#     t2 = h2 * 60 + m2
#     if(t1 == t2):
#         print("The difference: Both are Same !")
#         return
#     else:
#         difference = t2 - t1
#     h = (int(difference/60)) % 24
#     m = difference % 60

#     print("The difference:", h,":",m, "\n")
# time_difference(4, 15, 6, 7)

#que6. Python Program to Create a Lap Timer
# import time
# start=time.time()
# last=start
# num=1
# print("Press ENTER to count lap timer.\nPress CTRL+C TO stop")

# try:
#     while True:
#         input() 
#         lap= round((time.time()-last),2)
#         total=round((time.time()-start),2)
#         print("Lap number"+str(lap))
#         print("Total time taken:"+str(total))
#         print("Lap time:"+str(lap))
#         print("*"*20)
#         last=time.time()
#         num+=1
# except KeyboardInterrupt:
#     print("Process stopped")

#que7. Convert date string to timestamp in Python
# import datetime

# date_time_str = '2022-08-07 02:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)

# from datetime import datetime

# datetime_str = '09/19/18 13:55:26'

# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

# print(type(datetime_object))
# print(datetime_object)

# from datetime import datetime

# # Getting the current date and time
# dt = datetime.now()
# # getting the timestamp
# ts = datetime.timestamp(dt)

# print("Date and time is:", dt)
# print("Timestamp is:", ts)

#que8. How to convert timestamp string to datetime object in Python
# from datetime import datetime
# times_tamp = 1617295943.17321
# print(times_tamp)
# date_time=datetime.fromtimestamp(times_tamp)
# print("convert timestamp string to datetime object.")
# print("Date Time :",date_time)

#que9. Find number of times every day occurs in a Year.
# import datetime
# import calendar
# def day_occur_time(year):
#     days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
#     l=[52 for i in range(7)]

#     pos=-1
#     day = datetime.datetime(year, month = 1, day = 1).strftime("%A")
#     for i in range(7):
#         if day==days:
#             pos=i
#     if calendar.isleap(year):
#         l[pos]+=1
#         l[(pos+1)%7]+=1
#     else:
#         l[pos]+=1
#     for i in range(7):
#         print(days[i],l[i])
# day_occur_time(2022)      



##---------------------------- ASSIGNMENT ON FILE HANDLIND------------------------#
#1. Python program to read file word by word
# try:

#     with open('demo_write.txt','r') as fp:
#         for line in fp:
#             for word in line.split():
#                 print(word,end=' ')
# except FileNotFoundError as e:
#     print(e)

#2. Python program to read character by character from a file
# try:
    #with open("demo_multilines.txt",'r') as file:
#         while 1:
#             char = file.read()
#             if not char:
#                 break
#             print(char)
#         file.close()
# except Exception as e:
#     print(e)
#---------- OR -----------------------
    # for i in file.read():
    #     print(i,end=' ')
    # file.close()    

       
# que.3. Python – Get number of characters, words, spaces and lines in a file
# count_char=0
# count_words=0
# count_space=0
# count_lines=0

# try:
#     with open("demo_multilines.txt",'r') as fp1:
        
#         for  char in fp1:
#             if char.isspace():
#                 count_space+=1
           
#             words=char.split()
#             count_lines+=1
#             count_words=len(words)

            
#             count_char=len(char)
#         print("count of all characters :",count_char,"count_words :",count_words,"count of spaces between to words :",count_space,"count of lines :",count_lines)

# except FileExistsError as e:
#     print(e)
        

# que.4. Python | Finding ‘n’ Character Words in a Text File
# try:
   
#     with open("demo_multi.txt",'r') as file:
#         n=7
#         print("word length 7 :")
#         for char in file:
#             con_word=char.split()
            
#             for word in con_word:
#                 if (len(word))==n:
#                     print(word)
    
# except Exception as e:
#     print(e)

# que.5. Python Program to obtain the line number in which given word is present
# import logging
# logging.basicConfig(filename='log8.log',filemode='w',level=logging.DEBUG,datefmt='%d-%b-%Y %I:%M:%S %P')
# logging.getLogger()

# try:
#     file = open('demo_multi.txt','r') 
#     text = file.readlines()
#     word = 'python' 
#     for line in text: 
#          if word in line: 
#              print(text.index(line)+1)
# except FileNotFoundError as e:
#      logging.error(e)

# que.6. Count number of lines in a text file in Python
# try:

#     with open("demo_multi.txt",'r') as file:
#             count_lines=0
#             for line in file:
#                 count_lines+=1
#             print(count_lines)
# except FileNotFoundError as e:
#     print(e)

#que.7. Python Program to Eliminate repeated lines from a file
# try:
#     fp=open('text1.txt','w')
#     with open('textfile.txt','r') as file:
#         dup_line=set()
#         for line in file.readlines():
#             if line not in dup_line:
#                 fp.write(line)
#                 dup_line.add(line)
#     fp.close()
# except FileNotFoundError as e:
#     print(e)


# que.8. Python – Append content of one text file to another
# try:
#     fp1=open('demo_multi.txt','r')
#     fp2=open('text1.txt','r')
#     fp1.close()
#     fp2.close()
#     fp1=open('demo_multi.txt','a+')
#     fp2=open('text1.txt','r')
#     fp1.write(fp2.read())
#     fp1.seek(0)
#     fp2.seek(0)
#     fp1.close()
#     fp2.close()
# except Exception as p:
#     print(p)
    
#que.9. Python program to copy odd lines of one file to other
# try:
#     fn1=open('text1.txt','r')
#     fn2=open('demo_multi.txt','w')
#     count=fn1.readlines()
#     for i in range(0,len(count)):
#         if i%2!=0:
#             fn2.write(count[i])
#         else:
#             pass
#     fn2.close()

#     fn2=open('demo_multi.txt','r')
#     count1=fn2.read()
#     print(count1)
#     fn1.close()
#     fn2.close()

# except FileExistsError as a:
#     print(a)

#que.10. Python Program to merge two files into a third file

# try:
#     data=data2=" "
#     with open('demo_multi.txt','r') as f1:
#         data=f1.read()
#     with open('demo_multi.txt','r') as f2:
#         data2=f2.read()
#     data+='\n'
#     data+=data2    
#     with open('merge.txt','w') as file:
#         file.writelines(data)
    
# except FileNotFoundError as f:
#     print(f)

#que1. Python program to Reverse a single line of a text file
# try:
#     with open('demo_multi.txt','r+') as fp1:

#         r=fp1.readlines()
#     with open('new_text.txt','w+') as fp2:
#         fp2.writelines(r[::-1])
#         fp2.readlines()
# except FileExistsError as e:
#     print(e)

#que12. Python program to reverse the content of a file and store it in another file.
# try:
#     with open('demo_multi.txt','r') as f:
#         result=f.read()
#     data=result[::-1]
        
#     with open('reverse.txt','w') as f1:
#         f1.write(data)

# except Exception as m:
#     print(m)

####----------------------------------Scenario Based Programs---------------------------------------------------#####
#que1. Python Program for Linear Search
# lineare search:-Linear search is a method of finding elements within a list. It is also called a sequential search. 
#  It is the simplest searching algorithm because it searches the desired element in a sequential manner.
#The elements in the list must be sorted to apply the binary search algorithm. If elements are not sorted then sort them first.

#def linear_search(lst,key,n):
#     for i in range(0,n):
#         if (lst[i] == key):
#             return i
#     return-1

# lst=[1,3,6,5,7,9]
# n=len(lst)
# key=int(input("Enter Search Element:"))
# res=linear_search(lst,key,n)
# if res==-1:
#     print("Element not found.")
# else:
#     print("Element found at index:",res)

#que2.Python Program for Binary Search (Recursive and Iterative)
# binary:-A binary search is an algorithm to find a particular element in the list. Suppose we have a list of thousand 
# elements, and we need to get an index position of a particular element. We can find the element's index position very 
# fast using the binary search algorithm.

#------------Iterative Binary Search
# def binary_search(lst1,n):
#     low=0
#     mid=0
#     high=len(lst1)-1

#     while low<=high:
#         mid=(high+low)//2

#         if lst1[mid]<n:
#             low=mid+1

#         elif lst1[mid]>n:
#             high=mid-1

#         else:
#             return mid
#     return -1

# lst1=[20,24,28,31,35,45,90,100]
# n=int(input("Enter search element:"))
# res=binary_search(lst1,n)
# if res != -1:
#     print("Element found at indesx:",res)
# else:
#     print("Element not found.")

#---------------Recursive Binary Search
# def recursive_binary(lst,low,high,n):
#     if low<=high:
#         mid=(high+low)//2
        
#         if lst[mid] == n:
#             return mid

#         elif lst[mid]>n:
#             return recursive_binary(lst,low,mid-1,n)
#         else:
            
#             return  recursive_binary(lst,high,mid+1,n) 
#     else:
#         return -1

# lst=[12, 24, 32, 39, 45, 50, 54] 
# n=int(input("Enter search element:"))
# res=recursive_binary(lst,0,len(lst)-1,n)
    
# if res != -1:
#     print("Element present at index:",res)

# else:
#     print("Element not present.")


#que3. Python Program for Bubble Sort.
# bubble sort:-The bubble sort uses a straightforward logic that works by repeating swapping the adjacent elements 
# if they are not in the right order. It compares one pair at a time and swaps if the first element is greater than 
# the second element; otherwise, move further to the next pair of elements for comparison.

# def bubble_sort(lst):
#     for i in range(0,len(lst)-1):
#         for j in range(len(lst)-1):
#             if (lst[j]>lst[j+1]):
#                 temp=lst[j]
#                 lst[j]=lst[j+1]
#                 lst[j+1]=temp
#     return lst

# lst= [5, 3, 8, 6, 7, 2]  
# print("lst=",lst)
# print("bubble sort=",bubble_sort(lst))

## ---- or--------
# def bubble_sort(lst1):
#     for i in range(0,len(lst1)-1):
#         for j in range(len(lst1)-1):
#             if (lst1[j]<lst1[j+1]):
#                 lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
#     return lst1
# lst1=[10,3,90,46,4,7]
# print("bubble sort:",bubble_sort(lst1))


# que4. Write a python program for string that will print out char with char count.E.g. c Output should be a4b1a1h5
# str1= 'aaaabahhhhhaaa'
# str2=''
# temp=str1[0]
# count=0
# for i in str1:
#     if i == temp:
#         count+=1
#     else:
#         str2=str2+temp+str(count)
#         count=1
#         temp=i
# str2=str2+i+str(count)
# print(str2)
            

#que5.Write a python program to take command line arguments. (using docopt and otherlibraries). Two or more programs.
# 6. Write a python program to take input date string, time string is in UTC format we need to
#convert it into PST and print converted date time. E.g. input: “2023-02-13 18:10:27”
# from datetime import datetime
# import pytz

# today=datetime("2023-02-13 18:10:27",tzinfo=pytz.PST)
# print(today)
            
#7. write a program for character count string "aaabbbccaa" for output:a5b3c2


