#!/bin/python
import sys

def max_to_choose(arr):
    # Make a list (initially of zeros) to store the number 
    # of integers of that number *plus* the integers one 
    # number above. Then, after checking all the numbers in 
    # the input array, and adding one in the appropriate 
    # indices, I simply return the maximum count.
    # (note that we're given in the problem statement that 
    # the range of possible numbers is 1-99 inclusive)
    counts = [0]*99
    for i in range(len(arr)):
        if arr[i] > 98:
            counts[98] += 1
        else:
            counts[arr[i]-1]+=1
            counts[arr[i]]+=1
    return max(counts)

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

print max_to_choose(a)
