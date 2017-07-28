#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    # For this problem, I just need to determine whether 
    # the distance between the two kangaroos decreases, 
    # and at what rate. If that rate is sufficient to 
    # put them at the same position at the same step num
    diff = x2-x1
    vdiff = v2-v1
    
    # If the distance between them will forever increase,
    # then we can obviously just conclude they're never 
    # end up on the same space at the same time.
    if vdiff >= 0:
        return "NO"
    else:
        nsteps = float(diff)/float(vdiff)
        # You also need something to catch the cases 
        # where the kangaroos are so far apart that 
        # they can't arrive on the same space at the 
        # same step number!
        if abs(nsteps-round(nsteps))==0.0:
            if (x1+(v1*abs(nsteps))) == (x2+(v2*abs(nsteps))):
                return "YES"
        else:
            return "NO"

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
