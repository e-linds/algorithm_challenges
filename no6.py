#Given a singly linked list, Your task is to remove every K-th node of the linked list. 
#Assume that K is always less than or equal to length of Linked List.

#ok - so to remove the node, we will just reset head.next to equal head.next.next
#this means that we will address the node removal when head.next is the kth element
#we can move through the linked list and count each move

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def display_list(head):
    
        print(head.data)
        head = head.next
        if head:    
            display_list(head)


def display_list_2(head):

    while head:
        print(head.data)
        head = head.next


def solution(head, k, count = 1):

    # if head == None:
    #     return None
    
    if k == 1:
        return None
    
    elif head.next:
        count = count + 1
        if count == k:
            head = head.next
            count = 1
            solution(head, k, count)
        else:
            solution(head.next, k, count)


    else:
        print(head)
        return(head)
    

def solution_2(head, k):
    node = head

    count = 1

    if k == 1:
        return None
    
    while node:
        count = count + 1
        if count == k and node.next:
            node.next = node.next.next
            count = 1
        node = node.next

    return head


if __name__ == '__main__':

    head = Node(1)
    current = head

    for each in range(2,39):
        current.next = Node(each)
        current = current.next
    

    display_list_2(head)
    print("solution:")

    display_list_2(solution_2(head, 5))








        


    



    

    

    


        
