# Longest Polindromic Subsequence in Python
"""
Statement: FInd the longest palindromic subsequence
Subsequence: a sequence that can be driven from another sequence by deleting some elements
             without changing the order of them.
- Palindrome is string that reads the same backwards as well as forward.
"""

def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s[startIndex] == s[endIndex]:
        return 2 + findLPS(s, startIndex+1, endIndex-1)
    else:
        op1 = findLPS(s, startIndex, endIndex-1)
        op2 = findLPS(s, startIndex+1, endIndex)
        return max(op1, op2)

def findLPS_string(s, startIndex, endIndex):
    if startIndex > endIndex:
        return ""
    elif startIndex == endIndex:
        return s[startIndex]
    elif s[startIndex] == s[endIndex]:
        return s[startIndex] + findLPS_string(s, startIndex+1, endIndex-1) + s[endIndex]
    else:
        op1 = findLPS_string(s, startIndex, endIndex-1)
        op2 = findLPS_string(s, startIndex+1, endIndex)
        return op1 if len(op1) > len(op2) else op2

print(findLPS("ELRMENMET", 0, 8))
print(findLPS_string("ELRMENMET", 0, 8))
print(findLPS("APNA", 0, 3))
print(findLPS_string("PANA", 0, 3))