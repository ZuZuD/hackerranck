#!/usr/bin/env python
'''
URL: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

INPUT:
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6 

TESTCASE 01

Average = (97 +50 + 91 + 72 + 80)/5 = 78.00
Can you solve this challenge in 4 lines of code or less?
NOTE: There is no penalty for solutions that are correct but have more than 4 lines.
'''

from collections import namedtuple
length = int(input())
Student = namedtuple('Student', input().split())
li = [Student(*input().split()) for i in range(length)]
print('{:.2f}'.format(sum([int(std.MARKS) for std in li])/length))
