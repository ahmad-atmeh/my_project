import time 

# 1
class User:

#2
     def __init__(self,first_name,last_name):
         self.first_name=first_name
         self.last_name=0
         #3
         self.phone=id(self)
         self.card="5151664"
         self.login_attempts = 0

     def describe_user():
         print(f"the first name is {self.first_name} ")
         print(f"the last name is {self.last_name}")
         print(f"the phone  number is {self.phone} ")
         print(f"the card number is {self.card}")


     def greet_user():
         print(f"{self.first_name} you welcome in any time vist my profile ")


     def increment_login_attempts(self):
         self.login_attempts += 1
         print(f" the {self.first_name}  of login_attempts after increment is : {self.login_attempts}")
        
     def reset_login_attempts(self):
         self.login_attempts = 0
         print(f"the {self.first_name.title()} value of reser its : {self.login_attempts}")






user1=User("Ranger","killer") 
user2=User("jaks","fighter")
user3= User("ahmad","atmeh")
      

users = [user1,user2,user3]

for user in users:
    user.greet_user()
    user.describe_user()
    

users_logins =[(user1,5),(user2,3),(user3,1)]

for login in users_logins:
    user , number_of_login = login   #unback tuple  / cane use index  / of for loop
    user.describe_user()
    for n in range(number_of_login):
        if user.login_attempts <= 3:
            print("login in")
            time.sleep(1)
            user.increment_login_attempts()
        elif:
            print(f" max number ")
            time.sleep(5)
            user.reset_login_attempts()
            
               
            



name.describe_user()
name.greet_user()

name.increment_login_attempts()
name.increment_login_attempts()
subject.increment_login_attempts()
name.increment_login_attempts()
subject.increment_login_attempts()




name.reset_login_attempts()
subject.reset_login_attempts()





    