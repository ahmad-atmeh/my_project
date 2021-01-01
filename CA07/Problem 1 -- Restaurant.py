class Restaurant:
    
  

    def __init__(self, name , cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    

    def describe_restaurant(self):
        print(f"the restaurant_name is {self.name} ")
        print(f"the pieces  of cuisine_type is{self.cuisine_type}")



    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self,served):
        if served > self.number_served:
             self.served = served 
             print(f"you have anumber fo served {self.number_served}")
        elif served < self.number_served:
            print(f" cnot served the number of {self.number_served}  ")
        else:
            print(served)    
              

    def increment_number_served(self):
        self.number_served=self.number_served + 1



restaurant = Restaurant("ithaa undersea restaurant","Shrimp")

print(f"this is  name of the restaurant   :{restaurant.name}" )
print(f" this is type of the cuisine  the type is {restaurant.cuisine_type}")

Mansaf = Restaurant("slole","Eate")
chicken = Restaurant("fasst","Chicken")
Meat = Restaurant("best","Meat")

Mansaf.describe_restaurant()
chicken.open_restaurant()

gests =["nicola tisla","Albert enshtine","leonardo da vinci"]
print(f"the number of served Mansaf {Mansaf.number_served}")

for i in gests:
    print(f" {Mansaf.name.title()} served {i.title()} ")
    Mansaf.increment_number_served()

print(f"{Mansaf.name.title()} and number of served is  {Mansaf .number_served}")
    




Mansaf.describe_restaurant()
chicken.describe_restaurant()
Meat.describe_restaurant()



Restaurant.number_served = 8
print(Mansaf.number_served)

print(chicken.number_served)
print(Meat.number_served)

Mansaf.set_number_served(10)
print(f"the number of served is {Mansaf.number_served}")

chicken.increment_number_served()
print(f"the number is served in day and weak is {chicken.number_served}")