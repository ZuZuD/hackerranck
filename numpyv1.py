import numpy
# exemple input : 3 3 3
line = raw_input().split()
print numpy.zeros(eval(",".join(line)), dtype = numpy.int) #Type changes to int
print numpy.ones(eval(",".join(line)), dtype = numpy.int) #Type changes to int
