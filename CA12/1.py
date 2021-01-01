#1. Write a program that reads the lines from flatland.txt and displays only those lines that contain the word
#  Triangles, Squares, Pentagons, Hexagons. Ignore the cases of the words.


file_name= "flatland.txt"
my_file = open(file_name,"r")
list_word = ["Triangles" , "Squares", "Pentagons" , "Hexagons"]
for line in my_file:
    for word in list_word:
        if word in line.lower():
            print(line.split())

