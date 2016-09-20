#! /usr/bin/python
from itertools import *
num = 'a b c d'
#print [i for i in itertools.izip([j for j in num.split(" ")],[j for j in num.split(" ")])]
print [i for i in combination([j for j in num.split(" ")],[j for j in num.split(" ")])]
