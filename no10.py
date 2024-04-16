#Given a string s, find the first non-repeating character in it and return its index. 
#If it does not exist, return -1.

def solution(s):
    letters = {}

    for each in s:
        letters[each] = s.count(each)
        # print(each)

        # print(letters)
        # print(letters.keys())

        values = list(letters.values())
                
        if values.count(1) == 0:
            return -1

        for each in letters:
            if letters[each] == 1:
                # print(s.index(each))
                return s.index(each)
            
    