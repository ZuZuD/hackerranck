#!/usr/bin/env python
import sys

N = int(raw_input().strip())
if (N % 2 != 0):
    print "Weird"
elif (N >= 2 and N <= 5) or (N > 20):
    print "Not Weird"
else:
    print "Weird"
