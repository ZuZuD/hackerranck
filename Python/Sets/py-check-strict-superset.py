#!/usr/bin/env python
res = True
for i in range(int(raw_input())):
    A = set(raw_input().split())
    if not lis.issuperset(A):
        res = False
print res
