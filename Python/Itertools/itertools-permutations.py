#!/usr/bin/env python
A = map(str, raw_input().split())
liste = str()
for elt in list(itertools.permutations(sorted(A[0]), int(A[1]))):
    print("".join(elt))
