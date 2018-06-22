'''TUPLE'''

#1) Write a program to create a tuple with different data types and do the following operations.
#● Find the length of tuples

tup1 = ("Gritesh",21,"CSE",9.34)
print(tup1)
print("Length of above tuple : ",len(tup1))


#2) Find largest and smallest elements of a tuples.

tup2 = (10,15,48,6,25,14,20)
print("\n",tup2)
print("Maximum element above : ",max(tup2))
print("Minimum element above : ",min(tup2))


#3)Write a program to find the product of all elements of a tuple.

z = 0
prod = 1
while(z<len(tup2)):
    prod = prod * tup2[z]
    z+=1
print("\nProduct of above tuple elements : ",prod)
print()



'''SET'''

##1) Create  two set using user defined values.
##● Calculate difference between two sets.
##● Compare two sets.
##● Print the result of intersection of two sets.

set1 = set()
[set1.add(input("Enter set1 element : ")) for x in range(5)]
print("\nSet 1 : ",set1)

set2 = set()
[set2.add(input("Enter set2 element : ")) for x in range(5)]
print("Set 2 : ",set2)

print("Set1 - Set2 : ",set1-set2)
print("Set2 - Set1 : ",set2.difference(set1))
print("Comparison : ",set1^set2)
print("Intersection : ",set1 & set2)



'''Dictionaries'''

##1) Create a dictionary to store name and marks of 5 students.

print("\nFirst Enter the Marks then the Name")
dict1 = {input("Enter Name : "):input("Enter Marks : ") for x in range(5)}
print("Dictionary : ",dict1)


##2) Sort the dictionary created in previous question according to marks.

from operator import itemgetter
print("Above dictionary sorted according to values : ",sorted(dict1.items(), key=itemgetter(1)))


##3) Count the number of occurrence of each letter in word "MISSISSIPPI".
##  Store count of every letter with the letter in a dictionary. 

word = "MISSISSIPPI"
dict2 = {}
for  x in word:
    if x in dict2.keys():
        dict2[x]+=1
    else:
        dict2[x] = 1

print("Frequency of letters in word : ",dict2)
