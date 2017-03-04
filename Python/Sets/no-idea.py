#!/usr/bin/env python
array = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
happy = 0
for elt in array:
    if elt in A:
        happy += 1
    elif elt in B:
        happy -= 1
print happy
