#!/bin/python

def get_weighted_mean(arr, wts):
    the_sum = 0
    for i in range(len(arr)):
        the_sum += arr[i]*wts[i]
    return float(the_sum)/float(sum(wts))

n = int(raw_input())
arr = map(int, raw_input().strip().split(' '))
wts = map(int, raw_input().strip().split(' '))

print round(get_weighted_mean(arr, wts), 1)
