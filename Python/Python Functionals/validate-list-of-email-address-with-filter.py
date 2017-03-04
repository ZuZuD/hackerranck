#!/usr/bin/env python3
import re

size = eval(input())
email = [input() for i in range(size)]
acceptedmail = []

for mail in email :
  if re.findall(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.\w{2,3}$',mail):
    acceptedmail.append(mail)
print(sorted(acceptedmail))
