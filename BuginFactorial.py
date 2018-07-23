#!Python3
#This program will create a text file called myProgramLog.
#Logging messages will be in the text file.

#Using debugging
#logging
#Bug in factorial
import logging
logging.basicConfig(filename = 'myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') #logging messages in 'myProgramLog.txt'
logging.disable(logging.CRITICAL) #CRITICAL disables all log messages

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total = 1
    for i in range(1,n + 1): #remove 1, to see log messages
        total *= i
        logging.debug('i is %s, total is %s' %(i, total))

    logging.debug('Return value is %s' %(total))
    return total

print(factorial(5))

logging.debug('End of program')