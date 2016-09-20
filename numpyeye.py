import numpy
line = raw_input().split()
# exemple input : 3 3 
print numpy.eye(int(line[0]),int(line[1]),k=0)
