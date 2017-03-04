#!/usr/bin/env python
import numpy

line = raw_input().split()
print numpy.eye(int(line[0]),int(line[1]), k=0)
