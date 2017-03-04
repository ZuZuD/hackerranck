#!/usr/bin/env python
a = set(map(int, raw_input().split()))
num = input()
b = set(map(int, raw_input().split()))
c = a.symmetric_difference(b)
for n in sorted(list(c)):
    print n
