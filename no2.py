#given a linked list and value n, find the value which is nth from the end of the linked list

# find last node

# count = 0
ll = []
# n = ""
def option1(head):
    if head.next:
        option1(head.next)
        count = count + 1
    else:
        
        for each in ll:
            if ll.indexOf(each) == count - n:
                return each
            

#not efficient
#time complexity 2n -> n

array = []
def option2():
    for each in ll:
        array.append(each)
    answer = array[len(array) - n]
    return answer

# same as above

def option3(head, n):
    count = 0
    if head.next:
        option3(head.next, n)
        if head:
            count = count + 1
            if count == n:
                return head

            
        






