#!/usr/bin/env python
import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
diago1=[]
diago2=[]
for tab in enumerate(a):
    for num in enumerate(tab[1]):
        if num[0] == tab[0]:
            diago1.append(num[1])
        if num[0] == (len(tab[1])-1)-tab[0]:
            diago2.append(num[1])
result1 = reduce(lambda x,y: x+y, diago1)
result2 = reduce(lambda x,y: x+y, diago2)
print (abs(result1-result2))
