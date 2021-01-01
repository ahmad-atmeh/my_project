# 2.You are given a 2D matrix as input. Write a function transpose(matrix) which computes and returns the transposed matrix
# Input: matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
# Return: matrix_transposed = [[1, 4], [2, 5], [3, 6], [4, 8]]




# matrix = [[1 , 2 , 3 , 4] , [4 , 5 , 6 , 8]]
# matrix_transposed = []
# def transpose(matrix):
#    for x in range(0 , len(matrix[0])):
#       matrix_transposed.append([matrix[0][x] , matrix[1][x]])
#    print(matrix_transposed)


# transpose(matrix)

# another solution 


matrix = [[1 , 2 , 3 , 4] , [4 , 5 , 6 , 8]]
m1=matrix[::3]
m2=matrix[1::]

matrix_transposed=[]
def transpose(matrix):
    for i in range(0,len(matrix[0])):
       matrix_transposed_row=[]
       for row in matrix:
          
          

    
    print(matrix_transposed)

transpose(matrix)  



