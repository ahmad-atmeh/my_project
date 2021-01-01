# Class Circle
import math
class Circle: 
    
    # TODO: Define an instance attribute for PI
   
      
    def __init__(self, radius=1.0):
      # TODO: Define an instance attribute for the radius
             self.PI=3.14
             self.radius=radius
             
        
    # TODO: Define the string representation method and print
    # r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}
    def __str__(self):
        return f"r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}"

    # TODO: Define a get_area() method and return the area
    def get_area(self):
        return  self.PI * (self.radius ** 2)
       

    # TODO: Define a get_circumference() method and return the circumference
    def get_circumference(self):
          return 2 * self.PI * self.radius
         
    
    # TODO: Define a set_color(color) method which sets the object attribute
    def set_color(self, color):
        self.color = color
             
    # TODO: Define a get_color() method which returns the object attribute
    def get_color(self):
        return self.color

# Playground

# TODO: Create two circles one with radius 3, and one with the default radius
c1=Circle(3)
c2=Circle()
# TODO: Set the colors of your circles using the setter method
c1.set_color('black')
c2.set_color('green')
# TODO: Print the colors of your circles using the getter method
print(f" the color of circles 1 is  {c1.get_color()}")
print(f" the color of circles 2 is  {c2.get_color()}")
# TODO: Print your circles. How does this work?
print(c1)
print(c2)

# TODO: Print the radius and areas of your cricles
print(f" the area of cricles is {c1.get_area()} and the radius is {c1.radius} ")
print(f" the area of cricles is {c2.get_area()} and the radius is {c2.radius} ")
# TODO: Print the circumference of your circles using the getter method
print(f" the area of circumference 1 is {c1.get_circumference()}")
print(f" the area of circumference 2 is {c2.get_circumference()}")
