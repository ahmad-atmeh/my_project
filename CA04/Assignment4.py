# 1.Write a program which reads a number (n) from the user and the print the sum of all numbers between 1 and n
# n =int(input("enter number"))

n = int(input("enter the number of n : "))
print(f"The sum of the number between 1 and {n} is {sum(range(1, n+1))}.")

# 2.Write a program which prints the following pattern for any given number, n = 5, for example
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("enter the number of n : "))
my_string=""
for i in range(1,n+1):
    # Concatenate the string
    my_string += str(i) + " "
    print(my_string)

# revers pattern
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("\r")

# 3.Write a program which prints the multiplication table of a given number (stop at 10)

num = int(input("Enter the number: "))
for i in range(1, 11):
   print(num,"X",i,"=",num * i)

#4.Given a list of numbers iterate over it and print numbers which are divisible by 5. If you find number greater than 150 stop the exit iteration.
list1 = [5,10,12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
     if i <= 150 and i % 5 == 0:
           print(f"the numbers id divisible by 5 = {i}")
          
     elif i % 5==0 :
          break
       
# #5.Given a list of numbers, reverse the list without using the reverse() method..

new_list = [5,10,12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
revers_list = []

for i in new_list:
    revers_list.insert(0, i)

print(f"{new_list} reversed is '\n' {revers_list}")

# # 6.Given a string, get the length of the string without using the len() function..

my_string = "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering."

length = 0

for c in my_string:
    length += 1

print(f"The length of my string is {length}."

# #7.Write a program which reads the age of 3 different people. Then print the oldest, and youngest between them.
a1, a2, a3 = [int(a) for a in input("Enter any 3 numbers: ").split()]

ages_list = [a1, a2, a3]

print(f"The oldest person is {max(ages_list)} years old.")
print(f"The youngest person is {min(ages_list)} years old.")

#8.rite a program which prints the absolute value of any given number n without using the abs() function .

x = -10
abs = x

if x < 0:
    abs = -x

print(f" absolute value of {x} is {abs}.")

#9.Given two lists, create a third list by picking an even-index element from the first list and odd-index element from second.

# first_list = [3, 6, 9, 12, 15, 18, 21]
# econd_list = [4, 8, 12, 16, 20, 24, 28]
# results_list = [6, 12, 18, 4, 12, 20, 28]

first_list = [3, 6, 9, 12, 15, 18, 21]
second_list = [4, 8, 12, 16, 20, 24, 28]

list_length = len(first_list)
results_list = []

for i in range(list_length):
    if i % 2 == 0:
        results_list.append(first_list[i])
    else:
        results_list.append(second_list[i])

print(results_list)


#10.Given two lists of equal size create a set which contains elements from both lists as a pair.

# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# results_set = {(2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64)}

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result_list = []
list_length = len(first_list)
i = 0

for i in range(list_length):
    my_tuple = (first_list[i], second_list[i])
    result_list.append(my_tuple)

print(sorted(set(result_list)))

# Another solution
# result_zip = list(zip(first_list, second_list))
# print(result_zip)