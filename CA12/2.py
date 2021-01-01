# 2.Adapt the code above to count how often the word Flatland (with any capitalization) occurs in the first 5 lines. Print only the number of occurrences of that word. Once it works,
#  remove the count so that you count the number of occurrences of the word in the text as a whole.
# Write a program that reads the contents of sentences.txt and writes exactly the same contents to the file sentences.tmp. Then open the file sentences.tmp and display the contents.

COLOMUN = []
ROW = [[] , [] , []]

for x in range(0 , 3):
	COLOMUN.append('#')
for y in range(0 , 3):
	ROW[0].append('#')
	ROW[1].append('#')
	ROW[2].append('#')
x1 = ROW[0][1]
x2 = ROW[1][1]
x3 = ROW[2][1]

x1_y1 = ROW[0][2]
x2_y2 = ROW[1][2]
x3_y3 = ROW[2][2]

y1 = ROW[0][0]
y2 = ROW[1][0]
y3 = ROW[2][0]

print('\t' + x1 + '\t' + x1_y1 + '\t' + y1)
print('\t' + x2 + '\t' + x2_y2 + '\t' + y2)
print('\t' + x3 + '\t' + x3_y3 + '\t' + y3)