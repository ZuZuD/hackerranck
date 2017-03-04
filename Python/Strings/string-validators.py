#!/usr/bin/env python
lis = list(["False"] * 5)
for letter in line:
    if letter.isalnum():
        lis[0] = "True"
    if letter.isalpha():
        lis[1] = "True"
    if letter.isdigit():
        lis[2] = "True"
    if letter.islower():
        lis[3] = "True"
    if letter.isupper():
        lis[4] = "True"
for elt in lis:
    print elt
