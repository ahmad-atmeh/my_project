# # 1.Create a function check_ten(n1, n2) which returns a Boolean True if the sum of the numbers is 10.

def check_ten(n1,n2):
    if n1+n2 == 10:
     return True
    else:
      return False

print(check_ten(5,6))
#2.Create a function sum_ten(n1, n2) which returns a Boolean True if the sum of the numbers is 10. Otherwise, return the actual sum value.      

def sum_ten(n1, n2):
    if n1 + n2 == 10:
        return True
    else:
        return  n1 +n2

 print(sum_or_max(2,6))       
#3.Create a function first_upper(astring) which returns the first letter in the string in upper case

def first_upper(astring):
   return astring.capitalize()

print(first_upper("ahmad"))

#4.Create a function last_two(astring) which returns the last two characters as a tuple. If there are less than two characters, return the value "Error".  
def last_two(astr):
    if len(astr) < 2:
        return False
    else:
        return (f"{(astr[-1],astr[-2])}")

print(last_two(input ("enter ")))  

# 5.Create a function seq_check(numbers) which when given a list of integers, returns True if the sequence [1,2,3] appears somewhere in that list.
list_number=[1,2,3,4,5,6,7,8,9]
def seq_check(numbers):
    for i in  range(0,len(list_number)-1) :
        if numbers[i] > numbers[i+1]:
            return False
    return True
            
print(seq_check(list_number))     

#6.Create a function compare_length(s1, s2) which returns the difference in length between the strings.
def compare_length(s1, s2):
    if s1 > s2:
        return  (abs(len(s1) - len(s2)))
    else:
       print("not found")        
 
print(compare_length(input("pleas entar the first  string:"),input("pleas entar the secaned string:")))

#7.Create a function sum_or_max(my_list), given a list, if the length of the list is even return the sum of the list. If the length is odd, return the maximum value in that list.
list_lingth=[1,3,4,5,6,7]
def sum_or_max(my_list):
    if  len(my_list) % 2 == 0:
        return sum(my_list)
    else:
        return max(my_list)
             
print(sum_or_max(list_lingth))

#8.Create a function which returns a list of all numbers between 1 and 50 that are divisible by 3.
list_divisible=[]
def divisible(of_list):
    for i in of_list:
        if i / 3 ==0:
            list_divisible.append(i)
        return list_divisible
lst=[]
for i in range(2,50):
    lst.append(i)
 
print(divisible(lst)) 



#9.Create a function which returns a list of all even number between x and y. Use the range() function.

number=[]
def between (x,y):
    for i in range(x+1,y):
        if i % 2 == 0:
            number.append(i)
    return number
 
print(between(int(input("pleas enter the first number ")),int(input("pleas enter the first number "))))
#10.Create a function which take a string as an argument, then prints a string where for every character in the original there are three characters.
def three (str):
    for i in str:
        print(i*3,end='')
 
three(input("pleas enter the string "))