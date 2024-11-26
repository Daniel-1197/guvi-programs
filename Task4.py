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

# 4. convert the UML diagram into python class and its methods
# Part - A
class TV:
    def __init__(self,brand,price,inches,onoff_status):
        self.brand = brand
        self.channel = 1           # default value
        self.volume = 50           # default value
        self.price = price
        self.inches = inches
        self.onoff_status = onoff_status

    def increase_volume(self):         # method to increase volume
        if self.volume < 100:
            self.volume += 1
            return f"Volume increased to {self.volume}"

    def decrease_volume(self):         # method to decrease volume
        if self.volume > 0:
            self.volume -= 1
            return f"Volume decreased to {self.volume}"

    def set_channel(self,channel):            # method to set the channel
        if 1 <= channel <= 50:
            self.channel = channel
            return f"Channel is set to {channel}"
        else:
            return "Channel not found"

    def reset_tv(self):                 # method to reset the TV
        return f"Resetting TV volume: {self.volume}, channel: {self.channel}"

    def status(self):                    # method to return the status
        return f"{self.brand} at channel {self.channel},volume {self.volume}"

# Part -B
class LedTV(TV):
    def __init__(self,brand,price,inches,onoff_status,screen_thickness,energy_usage,refresh_rate,viewing_angle,
                 backlight):
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

        TV.__init__(self,brand,price,inches,onoff_status)

    def display_details(self):                                      # method to display the details
        return (f"LedTV details: \n"
              f"Brand : {self.brand} \n" 
              f"Price : {self.price} \n"
              f"Inches : {self.inches} \n"
              f"On Off Status : {self.onoff_status} \n"
              f"Screen Thickness : {self.screen_thickness} \n"
              f"Energy Usage : {self.energy_usage} \n"
              f"Refresh Rate : {self.refresh_rate} \n"
              f"Viewing Angle : {self.viewing_angle} \n"
              f"Backlight : {self.backlight}")

Television = LedTV('Sony','42000','32','Off','5','80W',
                   '120Hz','wide','Full-Array')
print(Television.display_details())
print(Television.reset_tv())
Television.volume = 87
print(Television.increase_volume())
print(Television.decrease_volume())
print(Television.set_channel(34))
print(Television.status())
