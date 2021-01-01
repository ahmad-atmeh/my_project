import random
# Class Square
class Square:

    def __init__(self, length):
        # TODO: Define the instance attributes
        if length <1:
            print("please chose a bigger value ")
        else:
            self.length=length
        self.color=None
    def get_length(self):
        if hasattr( self,'length'):
            return self.length
        
        
    # TODO: Define the string representation method and print the details of your square
    def __str__(self):
        s1="""
 _______
|       |
|       |
|       |  
|_______|
        """
        
        s2= f"\nthe square length is {self.get_length()}\tthe color is {self.color}"
        return s1+s2

    # TODO: Define a find_area() method and return the area
    def find_area(self):
        return self.length*self.length
        

    # TODO: Define a find_perimeter() method and return the perimeter
    def find_perimeter(self):
        return 4*self.length
    
    # TODO: Define a set_color(color) method which sets the object attribute
    def set_color(self, color):
        self.color=color
    
    # TODO: Define a get_color() method which returns the object attribute
    def get_color(self):
        return self.color

# Playground

# TODO: Create two squares
#creating objects from class squares 
n=5
colors_list=['red','green','white','yellow','blue']
squares_list=[]
for i in range(1,n+1):
    square=Square(i)
    color=random.choice(colors_list)
    square.set_color(color)
    squares_list.append(square)

print(squares_list)
 
for square in squares_list:
    print(square)



# square_one=Square(5)
# square_two=Square(4)
# TODO: Set the colors of your squares using the setter method
#setting a color to square one and two

# square_one.set_color("green")
# square_two.set_color("red")

# TODO: Print the colors of your squares using the getter method
#printing the colors of the square 
# print(f"the color of square one is {square_one.get_color()}")
# print(f"the color of square two is {square_two.get_color()}")

# TODO: Print your squares. How does this work?
#printing the square informations  
# print(square_one)
# print(square_two)

# TODO: Print the length, width, and area of your squares
# print(f"square one  length  is :{square_one.length}\t width is :{square_one.length}\t the area is :{square_one.find_area()} ")
# print(f"square two length is :{square_two.length}\t width is :{square_two.length}\t the area is :{square_two.find_area()} ")
# # TODO: Print the perimeter of your circles using the find_perimeter() method
# print(f"square one  perimerter is {square_one.find_perimeter()} ")
# print(f"square two perimerter is {square_two.find_perimeter()} ")
