#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

#Ex:
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)

def rotate_matrix():

    index = n-1

   
    for each in range(0,index):
        matrix[index][0] = matrix[index-1][0]
        matrix[index][-1] = matrix[index-1][-1]
        #need to figure out how the above will handle beginning/end


