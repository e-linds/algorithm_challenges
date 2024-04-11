# IN PROGRESS
#You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
#There is at least one empty seat, and at least one person sitting.
#Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
#Return that maximum distance to the closest person.

#Example:
#Input: seats = [1,0,0,0,1,0,1]
#Output: 2

def find_seat(seats):
    seat_options = []
    index = -1
    count = 0
    for each in seats:
        chosen_seat = [0,0]
        #chosen seat will reflect starting index, then number of empty seats beginning with starting index
        index = index + 1
        if each == 0:
            count = count + 1
            chosen_seat = [index, count]
            seat_options.append(chosen_seat)
            print(chosen_seat)
        else:
            chosen_seat = [0,0]
            count = 0

    print(seat_options)
    current_high = [0,0]
    for each in seat_options:
        if each[1] > current_high[1]:
            current_high = each
    print(current_high)
    return current_high

example = [0,1,0,1,0,0,0,0,0,1,0,0,0,1]
find_seat(example)