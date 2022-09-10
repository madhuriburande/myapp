##  code for debug 
import logging
logging.basicConfig(filename='log1.log',format='%(asctime)s %(message)s',filemode='w',datefmt='%d-%b-%Y %H:%M:%S %p')  
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("www.google.com")



logging.basicConfig(filename='log12f.log',forma='%(asctime)s %(message)s',datefmt=('%d-%m-%y %A-%B-%I',))
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("This is debug")
