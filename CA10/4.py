
#4. You are given a list of integers. Write a function cumulative_sum(numbers) which calculates the cumulative sum of the list. The cumulative sum of a list numbers = [a, b, c, ...] can be defined as [a, a+b, a+b+c, ...].
# Input: numbers = [1, 2, 3, 4]
# Return: cumulative_sum_list = [1, 3, 6, 10]

lis = [1, 2, 3, 4]

from itertools import accumulate

print(list(accumulate(lis)))