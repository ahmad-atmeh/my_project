# Shopping List

# Your shopping list should keep asking for new items until nothing is entered (no input followed by enter/return key).
# The program should then print a menu for the user to choose one of the following options:
# (A)dd - To add a new item to the list.
# (F)ind - To search for an item in the list.
# (P)rint - To pretty print the list.
# (S)ort - To sort the list.
# (C)lear - To clear all items in the list.
# (Q)uit - To exit your program.

# TODO: Define a data structure to keep track of your shopping list.
shopping_list = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = input()
  
    shopping_list.append(ele) # adding the element 
print(shopping_list) 




# TODO: Implement a function to show the menu to the user, then wait for a valid user choice.
def show_menu():
  print("""please choose one of the following options:
            (A)dd - To add a new item to the list>
            (F)ind - To search for an item in the list.
            (P)rint - To pretty print the list.
            (S)ort - To sort the list.
            (C)lear - To clear all items in the list.
            (Q)uit - To exit your program.
        """)


# TODO: Implement a function to add an item to your shopping list.
def add_item(item):
    shopping_list.append(item)
    print(f"The item has successfully added to the list, the new list is:\t{shopping_list}\n")

# TODO: Implement a function to find an item in your shopping list.
def find_item(item):
    if any (item in s for s in shopping_list):
        return print(f"the {item} is in the list:")
    else:
        return print(f" the {item} is not in list:")

# TODO: Implement a function to pretty print your tabbed lits.
def print_list():
     print(f"The shopping list is:\t {shopping_list}")

# TODO: Implement a function to pretty print your tabbed lits.
def sort_list():
    print(f"The shopping list is:\t {shopping_list.sort()}")

# TODO: Implement a function to pretty print your tabbed lits.
def clear_list():
    shopping_list.clear()

# TODO: Implement a function which calls the exit() function.
def quit():
    print("Goodbye! Hope to see you again soon :).")
    exit()

while True:
    show_menu()
    option = str (input("whats your choice ").lower())
    print(f"you chose option {option.upper()}")
    if option == 'a':
        element = input("what do you want to add to the shopping list \n")
        add_item(element)

    elif option ==  'f':
        element = input("enter the element you want to find \n")
        find_item(element)
        
    elif option == 'p':
        print_list()

    elif option == 's':
        sort_list()
        
    elif option == 'c':
        clear_list
        
    elif option == 'q':
        quit()
