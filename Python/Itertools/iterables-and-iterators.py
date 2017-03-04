#!/usr/bin/env python
import decimal

num = input()
li = raw_input()
taille = input()
lis = [i for i in combinations([j for j in (li.split(" "))], taille)]
count = 0
for tup in lis:
    if 'a' in tup:
        count += 1
output = decimal.Decimal(float(count) / float(len(lis)))
print(round(output, 4))
