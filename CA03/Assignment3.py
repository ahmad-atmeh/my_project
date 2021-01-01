# Q1

# # Print the first and last elements.
lst=[11, 100, 99, 1000, 999]
print(f" print the first index {lst[0]} and last index {lst[4]}")


# # Append the value 10000 to the list. Then append 9999 to the list.

lst.append(10000)
lst.append(9999)
print(lst)

# #. Insert the value 2 at every even index in the list that is lower than 10
 
lst.insert(2,10)
print(lst)

# Print the list, then print the list sorted.
print(f"the lest{lst}" )
lst.sort()
print(f"the new sorted lst{lst}")

# # Count and print the number of times the element 2 appears in your list.
 
lst.count(2)
print()

# Print the sum of the values in your list.

print(f"the sum in list is {sum(lst)}")

# 2.Given a list, remove all duplicate element and create a tuple with the remaining values. Then find the minimum and maximum numbers in that tuple.

test_list = [87, 45, 41, 65, 94, 41, 99, 94]
print ("The original list is : " +  str(test_list)) 

test_list =list(set(test_list))
print("The list after removing duplicates : " + str(test_list))

new_tuple=tuple(test_list)
print(new_tuple)

print(f"the min {min(new_tuple)} and the max is {max(new_tuple)} from the tuple ")



#3.Given a sample dictionary, print if the value 200 exits.

dictionary = {'a': 100, 'b': 200, 'c': 300}

print(dictionary['b'])

# # 4. Unpack the following tuple then print the values 

another_tuple = (10, 20, 30, 40)
a,b,c,d = another_tuple
print(a,b,c,d)

# 5.Modify the value 22 inside the following tuple to 2222.

tuple_2222 = (11, [22, 33], 44, 55)
tuple_2222[1][0]=2222
print(tuple_2222)


# 6.Swap then print following two tuples.

first_tuple = (11, 22)
second_tuple = (99, 88)
print("the first_tuple",first_tuple)
print("the second_tuple",second_tuple)
first_tuple , second_tuple = second_tuple ,first_tuple

print("the second_tuple",second_tuple)
print("the first_tuple",first_tuple)

# 7.Given two lists of equal size create a set which contains elements from both lists as tuples in the set.

first_List = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
result_Set = set(tuple(zip(first_List, second_list)))
print(result_Set)



# 8.Given two sets, checks if one set is subset or superset of the other set. If a subset is found delete all elements from that set. 

one_set={1,2,3,4,5}
tow_set={1,2,3,4,5,6,7,8,9,10}
three_set=one_set.issubset(tow_set)
print(three_set)
print(one_set.clear)



# 9.Given a dictionary the following dictionary,
personal_info={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

# 1.Print when and where Plato was born.
print(personal_info.get('born'))


# 2.Change Plato's birth year from B.C. 427 to B.C. 428.
personal_info["born"]="-428"
print(personal_info)




# 3.Add the following item to the dictionary..
# "work": ["Apology", "Phaedo", "Republic", "Symposium"]

personal_info["work"]= ["Apology", "Phaedo", "Republic", "Symposium"]
print(personal_info)

# 4.Find and print how many keys there are in the dictionary.
keys = personal_info.keys()
print(keys)

# 5.Find and print the key with the highest value in the dictionary.
max_key = list(personal_info.keys())
print(max(max_key))

# 6.Find and print the key with the lowest value in the dictionary.
min_key = list(personal_info.keys())
print(min(min_key))

# Create a list for each element in the tuple, inside each list you should have the value repeated n+1 times where n is the index in the tuple.
my_tuple = ('a', 'b', 'c', 'd')
a_list = list(my_tuple[0]) * 1
print(a_list) 
b_list = list(my_tuple[1]) * 2
print(b_list)
c_list = list(my_tuple[2]) * 3
print(c_list)
d_list = list(my_tuple[3]) * 4
print(d_list)
# Join all of the lists together and print the final output.
join_all = a_list + b_list + c_list + d_list 
print(join_all)



