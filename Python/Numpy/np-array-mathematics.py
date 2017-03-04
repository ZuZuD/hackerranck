#!/usr/bin/env python
import numpy

size = map(int,raw_input().split())
alis = []
blis = []
for i in range(size[0]):
    alis.append(raw_input().split())
for i in range(size[0]):
    blis.append(raw_input().split())
a = numpy.array(alis, int)
b = numpy.array(blis, int)
print a + b
print a - b
print a * b
print a / b
print a % b
print a ** b
