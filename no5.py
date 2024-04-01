# find the height of a binary tree where one node equals one height

# ok so we start at the top and move through the tree recursively, checking whether head.left or head.right exists. As we move down, we add to a count. 
# when we find that neither child exists, we add the value of current count to an array and then reset count to zero
# then we find the largest value in the array. 

#import numpy as np


count = 0
heights = []
def solution(head):

    if head:
        if head.right or head.left:
            count = count + 1
            solution(head.right)
            solution(head.left)
            
        else:
            heights.append(count)

        np_heights = np.array(heights)

        return np.max(np_heights)




        

