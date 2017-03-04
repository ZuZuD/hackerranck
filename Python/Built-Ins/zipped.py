#!/usr/bin/env python
li = [map(float, raw_input().split(" ")) for i in range(y)]
for elts in zip(*li):
    sum = 0
    for elt in elts:
        sum += elt
    print sum / len(elts)
