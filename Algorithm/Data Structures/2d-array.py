#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.

def hourglassSum(arr):
  
  maxline = len(arr[0])-2
  maxcol = len(arr)-2
  result = []
  
  for i in range(maxcol):
    for j in range(maxline):
      sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
      sum += arr[i+1][j+1]
      sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
      # Can't initialize to 0 as the max could be negative
      result.append(sum)
        
  return max(result)
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
