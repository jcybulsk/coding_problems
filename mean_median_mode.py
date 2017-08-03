#!/bin/python

def get_mean(arr):
    narr = len(arr)
    return float(sum(arr))/float(narr)

def get_median(arr):
    arr_sort = sorted(arr)
    narr = len(arr)
    # Odd number of elements or even?
    # If even, then take the average of the two middle elements.
    if (narr % 2) != 0:
        return arr_sort[narr/2]
    else:
        return((arr_sort[(narr/2)-1] + arr_sort[narr/2])/2.0)

def get_mode(arr):
    arr_sort = sorted(arr)
    curr_ct = 1
    curr_mode = arr_sort[0]
    # In case of a tie for the mode, return only the smallest element.
    for i in range(len(arr)):
        the_ct = arr_sort.count(arr_sort[i])
        if the_ct > curr_ct:
            curr_mode = arr_sort[i]
            curr_ct = the_ct
    return curr_mode

n = int(raw_input())
arr = map(int, raw_input().strip().split(' '))

print round(get_mean(arr), 1)
print round(get_median(arr), 1)
print get_mode(arr)
