# # OOPS...CONCEPT
# # 1. create a python class called circle with constructor which will take a list as an argument for the task.
# # list is  [10,501,22,37,100,999,87,351]

class Circle:
    def __init__(self,*args):           #using init constructor with positional argument to list as argument
        self.args = args

Shape = Circle(10,501,22,37,100,999,87,351)  #declaring object for the class
print(Shape.args)

# 2. create proper member variables inside the task if required and use them when necessary.
# For example for this task create a class private variable named pi = 3.141

class Circle:
    def __init__(self):
        self.__pi = 3.141         # declaring a private variable named pi
        print(self.__pi)

Circle()                          # calling the class

# 3. From the given list create two methods area and perimeter which will calculate the area and perimeter.

given_lst = [10,501,22,37,100,999,87,351]
class Circle:
    def __init__(self,*args):
        self.args = args
        self.__pi = 3.141

    def area(self):                                               # method to calculate area
        for r in given_lst:
            print("Area: ",self.__pi * (r ** 2),"sq.units")       # Using the private variable 

    def perimeter(self):                                          # method to calculate perimeter
        for r in given_lst:
            print("Perimeter: ",2 * self.__pi * r,"units")

Shape = Circle(10,501,22,37,100,999,87,351)
Shape.area()
Shape.perimeter()
