##1. Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle:
    def __init__(self,rad):
        self.rad = rad
    def getArea(self):
        return 3.14*self.rad**2
    def getCircumference(self):
        return 2*3.14*self.rad

ob1 = Circle(10)
print("Area : ",ob1.getArea())
print("Circumference : %.2f"%ob1.getCircumference())


##2. Create a Student class and initialize it with name and roll number. Make methods to :
##● Display - It should display all informations of the student.

class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def display(self):
        print("\PerfLogsnName : ",self.name)
        print("Roll Number : ",self.roll)

ob2 = Student("Gritesh",11506836)
ob3 = Student("Avinash",11507090)
ob4 = Student("Shubham",11503739)

ob2.display()
ob3.display()
ob4.display()


## 3. Create a Temprature class. Make two methods :
##● convertFahrenheit - It will take celsius and will print it into Fahrenheit.
##● convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature:
    def __init__(self,f,c):
        self.f = f
        self.c = c
    def convertFahrenheit(self):
        return self.c*9/5 + 32
    def convertCelcius(self):
        return (self.
                f-32)*5/9

ob5 = Temperature(120,42)
print(" \n120 in Celcius : ",ob5.convertCelcius(),"\n42 in Fahrenheit : ",ob5.convertFahrenheit())


##**  4. Create a class MovieDetails and initialize it with Movie name , artistname,Year of release and ratings.
##Make methods to 
##● Display-Display the details.
##● Update- Update the movie details.

class MovieDetails:
    def __init__(self,mname,aname,yr,rt):
        self.mname = mname
        self.aname = aname
        self.yr = yr
        self.rt = rt
    def display(self):
        print("\nMovie Name : ",self.mname)
        print("Artist Name : ",self.aname)
        print("Year of release : ",self.yr)
        print("Rating : ",self.rt)
    def update(self):
        print("Update Details")
        self.mname = input("Update Movie Name : ")
        self.aname = input("Update Artist Name : ")
        self.yr = input("Update year of release : ")
        self.rt = input("Update rating : ")
        
ob6 = MovieDetails("Bahubali","Prabhas","2016","10")
ob6.display()
ob6.update()
ob6.display()

##5. Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
##●  Display expenditure and savings
##●  Calculate total salary
##●  Display salary

class Expenditure:
    def __init__(self,exp,sav):
        self.exp = exp
        self.sav = sav
    def display(self):
        print("\nExpenditure : ",self.exp)
        print("Savings : ",self.sav)
    def calSalary(self):
        return self.sav + self.exp
    def displaySalary(self):
        print("Total Salary : ",self.calSalary())

ob7 = Expenditure(37000,15000)
ob7.display()
ob7.displaySalary()



        











