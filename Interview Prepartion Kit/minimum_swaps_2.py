#!/bin/python3

""" https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_r=profile

Sample Input 0

4
4 3 1 2

Sample Output 0

3
"""

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# 1.look for lowest/highest values
# 2. associate an incide
# 3. replace missing indices
# 4. dict {indice: value, indice: value}

def minimumSwaps(arr):
    mini = min(arr)
    for elt, idc in enumerate(arr):
        if idc != elt:

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
