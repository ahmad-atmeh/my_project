
# 3.You are given a list of words. Write a function called find_frequencies(words) which returns a dictionary of the words along with their frequency.
# Input: find_frequencies(['cat', 'bat', 'cat'])
# Return: {'cat': 2, 'bat': 1}

# Creating an empty dictionary  
def find_frequencies(word):
    freq ={}
     

    for item in word: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1

    for key, value in freq.items(): 
        print ("% s : % s"%(key, value)) 

# Driver function 
word =['cat', 'bat', 'cat'] 

find_frequencies(word) 



