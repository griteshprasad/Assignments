##1) What is Time Tuple?

'''
Time tuple  in python is a tuple that stores time.
The time tuple contains 9 integer values indexed from 0 to 8.

Index      Value     Range

  0         year    Ex - 1995
  1         month    1-12
  2         day      1-31
  3         hour     0-23
  4         minute   0-59
  5         second   0-59/60
  6         weekday  0-6
  7         yearday  0-365
  8         DST      -1,0,1
'''

##2) Write a program to get formatted time.

import time

t = time.localtime()
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

##3) Extract month from the time.

t = time.localtime()
t = time.mktime(t)
print(time.strftime("\n%m i.e %b",time.gmtime(t)))


##4) Extract day from the time.

t = time.localtime()
t = time.mktime(t)
print(time.strftime("\nToday is : %A",time.gmtime(t)))


##5) Extract date (ex : 11 in 11/01/2021) from the time. 

t = time.localtime()
t = time.mktime(t)
print(time.strftime("\nToday is : %d",time.gmtime(t)))


##6) Write a program to print time using localtime method.

t = time.localtime()
t = time.mktime(t)
print(time.strftime("\n%r",time.gmtime(t)))


##7) ** Find the factorial of a number input by user using math package functions.

import math
print("Factorial is : ",math.factorial(int(input("\nEnter a number : "))))


##8) ** Find the GCD of a number input by user using math package functions.

print("The GCD is :
      ",math.gcd(int(input("\nEnter first number : ")),int(input("Enter second number : "))))


##9) Use OS package and do the following tasks:
##●  Get current working directory.
##●  Get the user environment.

import os
print("\n",os.getcwd())

import os
print("\n",os.environ["HOME"])
















