#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.
"""
Problem Statement:
Given N, find the number of ways to express N as a sum of 1, 3, 4
Example:
1.    N = 4
      Number of ways = 4 ({1,3}, {3,1}, {4}, {1,1,1,1})

2.    N = 5
      Number of ways = 4 ({4,1}, {1,4}, {1,1,3}, {1,3,1}, {3,1,1}, {1,1,1,1,1})

To make the base condition, we need to get some values already there
if
N=0 = 1
N=1 = 1
N=2 = 1 which is {1,1}
N=3 = 2 which is ({3}, {1,1,1})
"""
# Number Factor Problem  in Python

def numberFactor(n):
    # Why we are returning 1
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1+subP2+subP3

print(numberFactor(5))
