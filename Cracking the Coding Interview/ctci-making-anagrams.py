#!/usr/bin/env python3


def number_needed(a, b):
    count = 0
    for letter in a:
        if letter in b:
            b.pop(b.index(letter))
        else:
            count += 1
    return count + len(b)


a = list(input().strip())
b = list(input().strip())

print(number_needed(a, b))
