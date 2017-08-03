#!/bin/python

n = int(raw_input().strip())
the_strs = []
the_queries = []
for i in range(n):
    the_strs.append(raw_input().strip())

nqueries = int(raw_input().strip())
for i in range(nqueries):
    the_queries.append(raw_input().strip())
    
for x in the_queries:
    print the_strs.count(x)
