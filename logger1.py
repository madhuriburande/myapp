
import logging
logging.basicConfig(filename='log1.log',format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
str1="www.google.com"
logger.debug(str1)
logger.info("i am information level i.e info")
logger.warning("I am warinig level")
logger.critical("i am critical level")


## code for info

logging.basicConfig(filename='log1.log',format='%(asctime)s %(message)s',datefmt= '%d-%b-%Y %I:%M:%S:%p')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("i am info")

## code for warning
logging.basicConfig(filename='log1.log',format='%(asctime)s %(message)s',level=logging.DEBUG)
logging.getLogger()
var="Python"
logging.warning("%s raised an warning",var)




