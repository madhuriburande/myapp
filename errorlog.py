import logging
logging.basicConfig(filename='log3.log',filemode='w',level=logging.DEBUG,datefmt='%d-%b-%Y %I:%M:%S %P')
logging.getLogger()

try:
    a=10
    b=0
    c=a/b
    print("division of a and b",c)
except ZeroDivisionError as e: 
    logging.error(e)   