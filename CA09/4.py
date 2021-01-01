# 4.Iterate over the range(1, 100) and print the numbers. However, if the number is a multiple of 3, print Fizz instead. If the number is a multiple of 5, print Buzz. If the number is a multiple of both 3 and 5, print FizzBuzz.

# Input: None
# Print: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz 10 ...

for num in range(1,101):
    if num % 3==0 and num % 5==0:    # another seliotion num num % 15 == 0
        print("FizzBuzz")
    elif num % 5==0:
        print("Buzz")
    elif num % 3==0:
        print("Fizz")
    else:
       print(num)            