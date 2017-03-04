#!/usr/bin/env python

li = list(map(int,input().strip().split()))
print(sum(li)-max(li), sum(li)-min(li))
