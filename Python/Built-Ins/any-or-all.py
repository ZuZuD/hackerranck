#!/usr/bin/env python
li = raw_input().split(" ")
print(any([j == j[::-1] for j in li]) and all([int(i) >= 0 for i in li]))
