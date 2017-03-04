#!/usr/bin/env python3

import sys
n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
end_list=len(a)-1
for i in xrange(k):
    a.insert(0,a[end_list])
    a.pop()
for a0 in xrange(q):
    query=input()
    print a[query]
