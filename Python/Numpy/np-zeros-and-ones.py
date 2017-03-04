#!/usr/bin/env python
import numpy

line = raw_input().split()
print numpy.zeros(eval(",".join(line)), dtype = numpy.int)
print numpy.ones(eval(",".join(line)), dtype = numpy.int)
