# 3. You are given a sentence as input. Return a list of all words of even length.

# Input: Print every word in this sentence that has an even number of letters.
# Return: ['word', 'in', 'this', 'sentence', 'that', 'an', 'even', 'number', 'of']


s=input('Enter any santence : ')

s2=s.split()

print(s2)

x=[]

for i  in s2:

    if len(i)%2==0:

        x.append(i)

print(x)

# anther selution

sentence = "every word in this sentence that has an even number of letters"
even_words=[word for word in sentence.split() if len(word) % 2 == 0]

# for word in sentence.split():
#     if len(word) % 2 == 0:
#        even_words.append(word)

# print(f"list of enen words is : {even_words}")

print(f"list of enen words is : {even_words}")