#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
  
  length = n
  result = [ 0 for i in range(length) ]
  
  for lines in queries:
    
      # value to add is the last value of the list
      toadd = lines[-1]
      result = [ toadd + result[i] if i in range(lines[0]-1, lines[1]) else result[i] for i in range(length)]
      
  return max(result)

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
