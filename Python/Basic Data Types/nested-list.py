#!/usr/bin/env python
n = input()
dico = dict()
for _ in range(n):
    lis = list()
    lis.append(raw_input())
    lis.append(float(input()))
    dico[lis[0]] = lis[1]

smaller, greater = lis[1], lis[1]
for value in dico.values():
    if value < smaller:
        smaller = value
    if value > greater:
        greater = value

smaller2 = greater
for value in dico.values():
    if value == smaller:
        pass
    elif value <= smaller2 and value > smaller:
        smaller2 = value

names = list()
for name, value in dico.items():
    if value == smaller2:
        names.append(name)

names.sort()
for name in names:
    print name
