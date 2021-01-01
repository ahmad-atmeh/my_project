# 6.Ask the user for a lowercase string (s) as input. Create a function called check_palindrome(s) which returns the longest substring which is palindrome.

# Input: "I love python.nohtyp evol I Python is never odd or even"
# Return: "never odd or even"

def check_palindrome(s1):
    p_list=[]
    max=0
    for i in range(0,len(s1)):                        
 
            for j in range(0,len(s1)-i):
                x=s1[i:len(s1)-j]                       #sub string
                y=x[::-1]
 
                if x.replace(' ','')== y.replace(' ',''):        #string = reverse of it without spaces
                    if len(x)>max:                           
                        max=len(x)
                        p_list.append(x)
    return p_list[-1]
 
s1=' never odd or even I love python.nohtyp evol I Python is'
print(check_palindrome(s1))
s2='heloo python nohtyp iam esraa etoom mooteaarse'
print(check_palindrome(s2))