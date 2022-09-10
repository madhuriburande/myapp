import logging
logging.basicConfig(filename='log4.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.getLogger()

try:
    a=int(input("Enter the first number:"))
    b=int(input("enter the second number:"))
    c=a/b
except ValueError as e:
    logging.critical(e,"Please Enter the correct value")
except ZeroDivisionError as a:
    logging.error(a)


