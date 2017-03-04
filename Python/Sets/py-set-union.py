#!/usr/bin/env python
s = set(map(int, raw_input().split()))
m = input()
s1 = set(map(int, raw_input().split()))
print len(s.union(s1))
