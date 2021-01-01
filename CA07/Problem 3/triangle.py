# Class Triangle


class Triangle():
    
    # TODO: Implement __init__ for this class use a,b,c and for the length of the sides
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
          
    def __str__(self):

     tri = """
        *
        ***
        *****
        ******
        ********
        """
     value = f"the length os the side area {self.a},{self.b},{self.c}"
     sentens = f"the area is {self.find_area()} and the perimeter is {self.find_perimeter()}"
     return sentens + tri + value  

    # TODO: Implement find_area() for this class
    def find_area(self):
        s = self.find_perimeter()
        #  s(s – a)(s – b)(s – c) 
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
      
        return(area)

    # TODO: Implement find_perimeter() for this class
    def find_perimeter(self): 
        return (self.a + self.b + self.c ) / 2
        

          
        

    # TODO: Implement a print_triangle_type() method which prints 
    # the type of the triangle based on the length of the sides.
    # Hint: You can use the Pythagorean Theorum to find the type of triangle.
    # Hint: Read more https://www.geeksforgeeks.org/find-the-type-of-triangle-from-the-given-sides/
    def print_triangle_type(self):
        if self.a == self.b == self.c:
            print("Equilateral Triangle")
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print("Isosceles Triangle")    
        else:
            print("Scaline Triangle")        


how_many = int (input = ("please enter how many "))
list_Triangle = []
print(f"Now I'll for the length of the  {how_many} triangle.")
for i in range(how_many+1):
    #tarnary operater
    a , b , c =[ int(x) for x in input(f"please enter three length {i} like (1,2,3) ").split(',')]
    print(a,b,c)
    list_Triangle.append(Triangle(a,b,c))

for triangle in list_Triangle:
    print(triangle)


triangle = Triangle(3,5,4)
print(triangle.find_area())
triangle.print_triangle_type()








