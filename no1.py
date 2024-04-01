# insert a node in a sorted way into a sorted double linked list

#pass through dll and get length

value = ""

def get_location(dll):

    index = math.ceil(len(dll)/2)
    middle = dll[index]

    if value > middle and value < middle.next:
        middle.next = value
    # elif value > middle:


#option 2
        
def option2(head):

    if value > head and value < head.next:
        head.next = value
    else:
        option2(head.next)


# time complexity: n
        


