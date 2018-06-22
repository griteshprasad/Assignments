#1. Take 10 integers from user and print it on screen.

y = []
for x in range(10):
    y.append(int(input("Enter element : ")))
print("List : ",y)


#3. Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

print("\n\n")
lis = [int(input("Enter element : ")) for x in range(10)]
lis_sq = [x*x for x in lis]
print("List : ",lis)
print("List of Square : ",lis_sq)


#4. From a list containing ints, strings and floats,print the types of each element.

print()
list1 = ["Gritesh",21,9.34]
[print(x,type(x)) for x in list1]


#5. Using range(1,101), make a list containing even and odd numbers.

list2 = [x for x in range(1,101,2)]
print("\n\nOdd List : ",list2)
list3 = [x for x in range(2,100,2)]
print("Even List : ",list3)


#6. Print the following patterns:
'''
*
**
***
****
'''
print("\n\n")
[print("*"*x) for x in range(1,5)]


#7. Create a user defined dictionary and get  keys corresponding to  the value using for loop.

dict1 = {1:'one',2:'two',3:'three',4:'four',5:'five'}
print("\n\n",dict1)
print("Reversed : ",end = '')
{print(y,x) for x,y in dict1.items()}


#8. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that
#   element, if found. Iterate over list using for loop.

print("\n\n")
list4 = [input("Enter element : ") for x in range(10)]
x = input("\nEnter element to be deleted : ")

for y in range(len(list4)):
    if x==list4[y] :
        del list4[y]
        break;
print("After deletion : ",list4)



#2. Write an infinite loop.An infinite loop never ends. Condition is always true.

print("\n\n")
while(True):
    print("Infinite Loop",end=' ')







    
