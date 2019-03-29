#!/bin/python3


""" https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_r=profile

Sample Input 0

2
abba
abcd

Sample Output 0

4
0

"""

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    count = 0

    for size in range(1, len(s)):
        for indice in range((len(s)+1)-size):
            key = ''.join(sorted(s[indice:indice+size]))
            for i in range(indice+1, (len(s)+1)-size):
                key_cur = s[i:i+size]
                count += IsAnagram(key, key_cur)
    return count

def IsAnagram(key, key_cur):
    if key == ''.join(sorted(key_cur)):
        return 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
