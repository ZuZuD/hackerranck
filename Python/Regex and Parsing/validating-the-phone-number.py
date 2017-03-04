#!/usr/bin/env python3
import re

line_nbr = input()
list = []
for number in range(line_nbr):
    list.append(raw_input())

for num in list:
    if (re.search(r'^[789]{1}\d{9}$', str(num))):
        print('YES')
    else:
        print('NO')
