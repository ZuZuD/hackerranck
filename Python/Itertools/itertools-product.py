#!/usr/bin/env python
A = map(int, raw_input().split())
B = map(int, raw_input().split())
liste = str()
for elt in list(itertools.product(A, B)):
    if len(liste) != 0:
        liste += " "
    liste += str(elt)
print liste
