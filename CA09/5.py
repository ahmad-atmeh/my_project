#5. You are given a binary string (001011001011) as input, return a list of all substrings which start and end with a 1.

# Input: 001011001011
# Return: ['101', '1011', '1011001', '101100101', '1011001011', '']

string = input("enter the lest ")
str_list=[]
for i in range(0, len(string)) : 
        if (string[i] == '1') : 
  
            # Search for all possible ending point 
            for j in range(i+1, len(string)) : 
                if (string[j] == '1') : 
                      str_list.append(string[i:j+1])
          
print(str_list)

 


