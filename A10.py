##1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
from threading import *
import time

def thread():
    time.sleep(5)
    print("This is "+str(current_thread().getName()))

t1 = Thread(target = thread)
t1.start()



##2. Make a thread that prints numbers from 1-10, waits for 1 sec between

def numthread():
    for x in range(1,11):
        time.sleep(1)
        print(x)

print()
t2 = Thread(target = numthread)
t2.start()


##3. Make a list that has 5 elements.Create a threading process that prints the  5 elements of the list with a delay
#of multiple of 2 sec between each display.                                            
##Delay goes like 2sec-4sec-6sec-8sec-10sec

def delaythread():
    lis = [5,4,8,7,6]
    for x,y in zip(range(6),lis):
        time.sleep(2*x)
        print(y)

print()
t3 = Thread(target = delaythread)
t3.start()


##4. Call factorial function using thread.

import math

def fact():
    print("\nFactorial of 5 : ",math.factorial(5))

t4 = Thread(target = fact)
t4.start()

















