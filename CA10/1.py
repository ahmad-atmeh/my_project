# 1.Ask the user for an integer and then use a list comprehension to build a list with all even number smaller than n. Print the list to the user.
# Input: n = 10
# Print: your_even_numbers = [0, 2, 4, 6, 8]
x=int(input('Enter any number'))

s=[i for i in range(x) if i%2==0]

print(s)


