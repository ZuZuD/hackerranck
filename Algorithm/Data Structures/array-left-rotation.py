#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    offset = d % n
    li = []
    i, j = 0, 0
    for i in range(len(a)):
        li.append(a[((offset+i)%n)])
    print(' '.join([str(i) for i in li]))
