import logging
logging.basicConfig(filename="DebugLog.txt",level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(logging.CRITICAL)

logging.info("Starting of the program")

def fact(n):
    factorial=1
    for i in range(1,n+1):
        logging.debug('I is (%s),Factorial is (%s)' %(i,factorial))
        factorial*=i
        
    return factorial


factorialValue=fact(5)
print(factorialValue)

logging.info("Ending of the program")
