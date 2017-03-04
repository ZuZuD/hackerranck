#!/usr/bin/env python
tab = [[int(j) for j in raw_input().split()]for i in range(size[0])]
k = input()
order = sorted(range(len(tab)), key=lambda c: tab[c][k])
tab_sort = [tab[i] for i in order]
for elt in tab_sort:
    print str(elt).replace(",", "").replace("[", "").replace("]", "")
