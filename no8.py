#You are given a string s consisting only of uppercase English letters.
# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.
# Return the minimum possible length of the resulting string that you can obtain.
# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.


def solution(s):
       
    var = ""
    letters = list(s)
    while "AB" in s or "CD" in s:
        if "AB" in s:
            index = s.index("AB")
            del letters[index:index + 2]
            s = var.join(letters)
        if "CD" in s:
            index = s.index("CD")
            del letters[index:index + 2]
            s = var.join(letters)
    return len(s)