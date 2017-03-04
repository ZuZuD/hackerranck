#!/usr/bin/env python
import email.utils
import re

num = input()
list = []
for addr in range(num):
    list.append(raw_input())

for mail in list:
    new = re.sub(r'<|>', r'', mail)
    n = re.search(
        r'^\w+\s[a-zA-Z][a-zA-Z0-9_.-]*@[A-Za-z]+\.[a-zA-Z]{1,3}$',
        new)
    if n:
        print mail
