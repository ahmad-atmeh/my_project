# Guacamole Search

""" The linear search is used to find an item in a list. 
The items do not have to be in order. 
To search for an item, start at the beginning of the list and continue searching until either the end of the list is reached or the item is found.
"""


ingredients = ["1 tbsp cilantro", "2 avocados", "1 lime" , "1 tsp salt", "1/2 onion"]


# TODO: Implement the function which adds an ingredient to the list
def add_ingredient(ingredient):
    ingredients.append(ingredient)

# TODO: Implement the function which removes and returns the last ingredient in the list
def pop_ingredient():
    ingredients.pop()
    return print(f" pop the last element in list {ingredients}")
    


# TODO: Implement the function which removes and returns an ingredient at the given index
def pop_ingredient_at(index):
    ingredients.pop(index)
    return print(ingredients)

# TODO: Implement the function which counts and returns the number of needed ingredients
def count_ingredients():
    return(len(ingredients))
    

# TODO: Implement the function which print the number of ingredients needed and a tabbed list of ingredients
def pretty_recipe():
      print(f"the number of ingredients i needed is :{count_ingredients()}")
      for ingredient in ingredients :
          print(f"\t * {ingredient}")

    

# TODO: 
# * Implement the linear search algorithm on the list of ingredients.
# * Test that it works with ingredients in and not in the list.
# * Add a counter to keep track of how many searches have been done for each item searched for.
# * Add the functionality to add an item to the list if it is not found.

def search_for_ingredient(ingredient):
    count = 0 
    ingredient_found = False
    for i in ingredients:
        count +=1
        if i == ingredient:
            ingredient_found = True
            break
    if ingredient_found:
        print(f"found the ingredient {ingredient} after {count}")

    else:
        print("the ingreduent not found")
        add_ingredient(ingredient)
        






# TODO: Call your functions here to test your code.

# add_ingredient("1 tables tsp")
# print(f"add ingredients in list{ingredients}")
# pop_ingredient()
# pop_ingredient_at(0)
# print(count_ingredients())
search_for_ingredient("2 avocados")
search_for_ingredient("ahmad")
# pretty_recipe()
# print(count_ingredients())



