#!/bin/python3

"""https://www.hackerrank.com/challenges/common-child/problem?h_r=profile


Sample Input

HARRY
SALLY

Sample Output

 2
"""

import os

def commonChild(s1, s2):
    arr = [[0 for i in range(len(s1))] for y in range(len(s2))]
    for i, s1_letter in enumerate(s1):
        for j, s2_letter in enumerate(s2):
            if i == 0 or j == 0:
                if s1_letter == s2_letter:
                    arr[i][j] = 1
                elif i > 0:
                    arr[i][j] = arr[i-1][j]
                elif j > 0:
                    arr[i][j] = arr[i][j-1]
            else:
                if s1_letter == s2_letter:
                    arr[i][j] = arr[i-1][j-1]+1
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    # print_f(arr
    return arr[-1][-1]

# Debug - print the multi-dim array formatted
def print_f(arr):
    for i in arr:
        print(i)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()

