#1) Create a function to calculate the area of a circle by taking radius from user.

def circle_area(r):
    return 3.14*r*r

print("Area of Circle : ",circle_area(int(input("Enter radius of circle : "))))


#2) Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in
#    a program that determines and prints all the perfect numbers between 1 and 1000.
#    [An integer number is said to be “perfect number” if its factors, including 1(but not the number itself),
#    sum to the number. E.g., 6 is a perfect number because 6=1+2+3]. 

def perfect(n):
    summ = 0
    for x in range(1,int(n/2)+1):
        if n%x == 0:
            summ+=x
    if summ == n:
        return "Perfect Number"
    else:
        return "Not Perfect"

result = print(perfect(int(input("\nEnter a number : "))))

print("\nPerfect Numbers between 1 and 100 are : ")
for y in range(1,1000):
    result = perfect(y)
    if result == True:
        print(y)


#3) Print multiplication table of 12 using recursion.

def table(n):
    if n>0:
        table(n-1)
        print("12 x",n,"=",12*n)

table(10)
    

#4) Write a function to calculate power of a number raised to other ( a^b ) using recursion. 

def cal_pow(x,y):
    print(x,'^',y,'=',x**y)

x = int(input("\nEnter number : "))
y = int(input("Enter power : "))
cal_pow(x,y)


#5) Write a function to find factorial of a number but also store the factorials calculated in a dictionary 

def fact(n):
    if n == 0 or n == 1:
        return 1
    if n>0:
        return n*fact(n-1)

dicfac = {x:fact(x) for x in range(11)}
print("\nDictionary with numbers and their factorial : \n",dicfac)


















