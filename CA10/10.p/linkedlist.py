  
# Define a class for the linked list
from node import Node

# Class for a simple Linked List

class LinkedList:
    def __init__(self, data):
        self.start_node = Node(data)
        self.items = data
        self.ref = None 

    def traverse_list(self):
        if self.start_node is None:
            print("list has no element ")
        
        else:
                n = self.start_node
            while n is not None:
                print(n.items(), " ")
            n = n.ref  
         

    def insert_at_start(self, data):
        new_node =Node(data)
        new_node.ref =self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node =Node(data)
        if self.start_node is None:
            self.start_node = new_node 
            return 

        n = self.start_node 
        while n.ref is not None:
            n = n.ref
        n.ref = new_node




    def insert_after(self, x, data):
        pass

    def insert_before_item(self, x, data):
        pass
        
    def insert_at_index (self, index, data):
        pass

    def get_count(self):
        pass

    def search_item(self, x):
        pass

    def make_new_list(self):
        pass

    def delete_at_start(self):
        pass

    def delete_at_end(self):
        pass

    def reverse_linkedlist(self):
        pass



# Our linked list like this now
#   (40)->(10)->(5)->(3)-> None