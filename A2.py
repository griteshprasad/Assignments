#1) Create a list with user defined inputs.

list1 = [input("Enter element : ") for x in range(5)]
print("List : ",list1)


#2) Add the following list to above created list:
    #[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]

list1.extend(['google','apple','facebook','microsoft','tesla'])
print("\nExtended list : ",list1)


#3) Count the number of time an object occurs in a list.

import collections
list2 = [10,20,15,48,51,21,12,10,12,20,48,21,10,48]
print("\nFrequency of elements : ",collections.Counter(list2))


#4) Create a list with numbers and sort it in ascending order.
list2.sort()
print("\nSorted list : ",list2)


##5) Given are two one-dimensional arrays A and B which are sorted in
##    ascending order. Write a program to merge them into a single sorted array C
##    that contains every item from arrays A and B, in ascending order. [List]

list3 = [54,65,12,4,8,49]
list3.sort()

list4 = []

list4.extend(list2)
list4.extend(list3)
list4.sort()
print("\nMerged sorted list : ",list4)


#6) Implement a stack and queue using lists.

'''QUEUE'''
from collections import deque
print("\nCreating QUEUE")
list5 = deque([input("Enter element : ") for x in range(5)])
print("\nQueue : ",list5)
print("\nElement out : ",list5.popleft())
print("\nQueue : ",list5)

'''STACK'''
print("\nCreating STACK")
list6 = deque([input("Enter element : ") for x in range(5)])
print("\nStack : ",list6)
print("Element popped : ",list6.pop())
print("\nStack : ",list6)









