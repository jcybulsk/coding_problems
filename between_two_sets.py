#!/bin/python
import sys

def check_list_a(l,x):
    return list({x % i for i in l})

def check_list_b(l,x):
    return list({i % x for i in l})

def getTotalX(a, b):
    lena = len(a)
    lenb = len(b)
    count = 0
    # Now search for any integers that are multiples 
    # of all the elements of a, and which also serves 
    # as a factor for all elements of b.
    for i in range(a[lena-1],(b[0]+1)):
        resa = check_list_a(a,i)
        resb = check_list_b(b,i)
        if (resa==[0]) & (resb==[0]):
            count+=1
    return count

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
total = getTotalX(a, b)
print(total)
