import logging
logging.basicConfig(filename='log5.log',format='%(asctime)s %(message)s',level=logging.DEBUG)
logging.getLogger()

try:
    a=5
    b=0
    res=a/b
except Exception as e:
    logging.error(e)
