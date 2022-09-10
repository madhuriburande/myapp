## 1. Write a program to create a file with mode ‘w’ to write an error message.
import logging
logging.basicConfig(filename='log6.log',filemode='w',format='%(asctime)s %(message)s')
level=logging.ERROR
logging.error("This an error")

## 2.Write a program to create a logger and format the message with the date and the main message content.
logging.basicConfig(format='%(name)s %(message)s',level=logging.WARNING)
logging.getLogger('Logger:')
logging.warning("Warning!")