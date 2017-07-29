#!/bin/python
import sys

def timeConversion(s):
    # Take the last two elements of the string, and 
    # proceed differently if it's PM or AM.
    strlen = len(s)
    if s[(strlen-2):strlen] == "AM":
        s = s.replace("AM", "")
        if s[0:2] == "12":
            s = s.replace("12","00",1)
    else:
        s = s.replace("PM", "")
        if s[0:2] != "12":
            s = s.replace(s[0:2], str(int(s[0:2])+12), 1)
    return s

s = raw_input().strip()
print timeConversion(s)
