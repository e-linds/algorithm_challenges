#find whether a binary tree is balanced or not


def solution(head):
    if head.left and head.left > head:
        solution(head.left)
    if head.right and head.right < head:
        solution(head.right)
    
    if head.right < head or head.left > head:
        return False

    return True
    
