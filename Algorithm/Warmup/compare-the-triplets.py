#!/usr/bin/env python
import sys

li_alice = map(int,raw_input().strip().split(' '))
li_bob = map(int,(raw_input().strip().split(' ')))
dico = {'alice':0,'bob':0}
for i,j in enumerate(li_alice):
    if li_alice[i] > li_bob[i]:
        dico['alice']+=1
    elif li_alice[i] < li_bob[i]:
        dico['bob']+=1
print "{} {}".format(dico['alice'],dico['bob'])
