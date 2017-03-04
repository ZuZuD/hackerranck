#!/usr/bin/env python
A = map(str, raw_input().split())
liste = str()
for i in range(1, int(A[1]) + 1):
    for elt in list(itertools.combinations(sorted(A[0]), i)):
        print("".join(elt))
