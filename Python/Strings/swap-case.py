#!/usr/bin/env python
array = list()
for i, letter in enumerate(sentence):
    if letter.isupper():
        array.append(letter.lower())
    else:
        array.append(letter.upper())
print ("").join(array)
