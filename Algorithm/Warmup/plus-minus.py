#!/usr/bin/env python

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
result = {'above': 0, 'below': 0, 'equal': 0}
for i in arr:
    if i>0:
        result['above']+=1
    elif i<0:
        result['below']+=1
    else:
        result['equal']+=1
print "{:6f}".format(result['above']/float(n))
print "{:6f}".format(result['below']/float(n))
print "{:6f}".format(result['equal']/float(n))
