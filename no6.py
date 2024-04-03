#Given a singly linked list, Your task is to remove every K-th node of the linked list. 
#Assume that K is always less than or equal to length of Linked List.

#ok - so to remove the node, we will just reset head.next to equal head.next.next
#this means that we will address the node removal when head.next is the kth element
#we can move through the linked list and count each move

count = 1
k = ""
def solution(head):
    if k == 1:
        return None

    elif head.next:
        count = count + 1
        if count == k:
            head.next = head.next.next
            count = 1
        solution(head.next)
    
        
