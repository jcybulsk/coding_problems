#!/bin/python
import sys

lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
     's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nlc = len(lc)

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

cipher = ""
for i in range(len(s)):
    # Check if it's a letter or some other ASCII character
    if s[i].lower() in lc:
        # is it lower-case or upper-case?
        if s[i].islower():
            # Can I add K to the index and not run past the size 
            # of the alphabet array?
            if (lc.index(s[i])+k) <= (nlc-1):
                snew = lc[lc.index(s[i])+k]
            else:
                # If not, then consider only the remainder after 
                # dividing the index number by the size of the 
                # alphabet list.
                snew = lc[(lc.index(s[i])+k)%(nlc)]
        else:
            if (lc.index(s[i].lower())+k) <= (nlc-1):
                snew = lc[lc.index(s[i].lower())+k].upper()
            else:
                snew = lc[(lc.index(s[i].lower())+k)%(nlc)].upper()
    else:
        snew = s[i]
    cipher+=snew
print cipher
