##1) Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is
##    inheriting Animal and access the base class method.

class Animal:
    def animal_attribute(self):
        print("In class Animal")

class Tiger(Animal):
    def __init__(self):
        print("In class Tiger")
        self.animal_attribute()
        print("Again in class Tiger")

ob1 = Tiger()


##2) What will be the output of following code.
##class A:
##    def f(self):
##        return self.g()
##
##    def g(self):
##        return 'A'
##
##class B(A):
##    def g(self):
##        return 'B'
##
##a = A()
##b = B()
##print (a.f(), b.f())
##print (a.g(), b.g())
##
'''
Output :

A B
A B
'''



##3) Create a class Cop. Initialize its name, age , work experience Define methods to  display and update the
##following details. Create another class Mission which extends the class Cop. Define method add_mission _details.
##Select an object of Cop and access methods of base class to get information for a particular cop and make it
##available for mission. 

class Cop:
    def __init__(self,name,age,wexp):
        self.name = name
        self.age = age
        self.wexp = wexp
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Work Experience : ",self.wexp)
    def update(self):
        self.name = input("Update Name : ")
        self.age = int(input("Update Age : "))
        self.wexp = int(input("Update Work Experience : "))

class Mission(Cop):
    def addMissionDetails(self):
        print("One Cop is now available for Mission\n\nDetails of the Cop is given below")
        self.display()
        print("\nUpdate details of Cop on Mission")
        self.update()
        print("Cop ready for Mission with details")
        self.display()

ob3 = Mission("Gritesh",21,4)
ob3.addMissionDetails()



##4) Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle
##and square which inherits shape and access the method Area.

class Shape:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b

class Rectangle(Shape):
    def area(self):
        print("\n
              Area of Rectangle : ",super().area())
        
class Square(Shape):
    def area(self):
        print("Area of Square : ",super().area())

ob4 = Rectangle(20,15)
ob4.area()
ob5 = Square(5,5)
ob5.area()
















