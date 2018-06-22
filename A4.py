#1) Take an input year from user and decide whether it is a leap year or not.

year = int(input('Enter year : '))

if year%4 == 0 and not year%100==0:
    print('Leap year')
elif year%400==0:
    print('Leap Year')
else:
    print('Not leap year')


#2) Take length and breadth input from user and check whether the dimensions are of square or rectangle.

l = int(input('\nEnter Length : '))
b = int(input('Enter breadth : '))

if l == b :
    print('It\'s a square')
else:
    print("It's a rectangle")


#3) Take the input age of 3 people and determine oldest and youngest among them

age = [input("\nEnter age of Person "+str(x)+" : ") for x in range(1,4)]
if age[0] > age[1] and age[0] > age[2]:
    print("Person 1 is Oldest")
elif age[1] > age[2]:
    print("Person 2 is Oldest")
else:
    print("Person 3 is Oldest")

if age[0] < age[1] and age[0] < age[2]:
    print("Person 1 is Youngest")
elif age[1] < age[2]:
    print("Person 2 is Youngest")
else:
    print("Person 3 is Youngest")



#4) Write an if statement that lets a competitor know which of these prizes they won based on the number of points they
#scored, which is stored in the integer variable points(your input).  points can only take on positive integer values
#up to 200.If they've won a prize, the message should state "Congratulations! You won a [prize name]!"
#with the prize name. If there's no prize, the message should state "Sorry! No prize this time."

#Points	        Prize

#1 - 50	        No prize
#51 - 150	Wooden dog
#151 - 180	Book
#181 - 200	Chocolates

points = int(input("\nEnter the point you have scored (between 1 and 200): "))

if points in range(1,50):
    print("Sorry! No prize this time.")
elif points in range(51,150):
    print("Congratulations! You won a Wooden dog")
elif points in range(151,180):
    print("Congratulations! You won a Book")
elif points in range(181,200):
    print("Congratulations! You won a Chocolates")


#5) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity.
#Assume one unit will cost 100.Judge and print total cost for user.

quant = int(input("\nEnter total quantity : "))
cost = quant * 100

if cost > 1000:
    print("Total Amount with discount :",cost-(cost*0.1))
else:
    print("Total Amount :",cost)




