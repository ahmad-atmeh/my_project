# 9.Given a string with repeated characters as input, create a function shuffle_well() and return a rearranged string so that no two adjacent characters are the same.

# Input: aaabb or aa
# Return: ababa or "String cannot be rearranged."



def get_key(dic,max_val,pkey):
    for key ,valus in dic.items():
        if valus==max_val and pkey!=key :
            return key
    return ' '
 
def shuffle_well(s1):
    s2=set(s1)
    count_dic={}
    str1=''
    y=''
    x=0
    for i in s2:
        count_dic[i]=s1.count(i)
    
    for i in range(0,len(s1)):
        x=max(count_dic.values())
        while get_key(count_dic,x,y)==' ' and x>0:
            x-=1
        if x==0:
            x=-1
            break
        y=get_key(count_dic,x,y)
 
        count_dic[y] -=1
        str1 +=y
 
    if x==-1:
        print('cant be rearranged')
    else:
        print(str1)
 
s1="aaabb"
shuffle_well(s1)
s2="babababab"
shuffle_well(s2)