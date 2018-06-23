####1) Name and handle the exception occured in the following program:
####a=3
#### if a<4:
####    b=a/(a-3)
####     print(b)

'''
The exception occured in the above code is "ZeroDivisionError"
'''

a=3
try:
    if a<4:
        b = a/(a-3)
        print(b)

except:
    print("\n...ZeroDivisionError occured...")


####2) Name and handle the exception occurred in the following program:
####    l=[1,2,3]
####    print(l[3])

'''
Exception : IndexError 
'''

l = [1,2,3]
try:
    print(l[3])
except:
    print("\n...Index Out of bound exception occured...")



####3) What will be the output of the following code:		
##### Program to depict Raising Exception

####try:
####    raise NameError("Hi there")  # Raise Error
####except NameError:
####    print("An exception")

'''
OUTPUT : An exception
'''


##4) What will be the output of the following code:
##### Function which returns a/b

##def AbyB(a , b):
##    try:
##        c = ((a+b) / (a-b))
##    except ZeroDivisionError:
##        print("a/b result in 0")
##    else:
##        print(c)
##
##### Driver program to test above function
##AbyB(2.0, 3.0)
##AbyB(3.0, 3.0)

'''
OUTPUT : -5.0
         a/b result in 0
        
'''


##5) Write a program to show and handle following exceptions:
##● ImportError
##● Value Error
##● Index Error

l = [1,2,3,4]
try:
    print(l[4])
except(IndexError):
    print("\nIndex Error Encountred")

try:
    x = int("Gritesh")
except(ValueError):
    print("Value Error Encountered")

try:
    import oldSchool
except(ImportError):
    print("Import Error Encountered")










