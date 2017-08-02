#!/bin/python
import sys

def maximumToys(prices, k):
    toy_ct = 0
    tot_cost = 0
    while tot_cost <= k:
        tot_cost += prices[toy_ct]
        if tot_cost < k:
            toy_ct += 1
        else:
            if toy_ct > 0:
                return toy_ct
            
if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = sorted(map(int, raw_input().strip().split(' ')))
    result = maximumToys(prices, k)
print result
