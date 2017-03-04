#!/usr/bin/env python
motif = raw_input()
lis = list()
count = 0
for i in range(0, len(sentence)):
    lis.append(sentence[i])
    if len(lis) > len(motif):
        lis.pop(0)
    if "".join(lis) == motif:
        count += 1
print count
