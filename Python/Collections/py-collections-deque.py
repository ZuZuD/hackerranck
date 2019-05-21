#!/usr/bin/env python3

'''
URL:

Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Constraints

0 < N =< 100

Output Format

Print the space separated elements of deque d.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2
'''

from collections import deque
d = deque()
length = int(input())

for _ in range(length):
    cmd = input().split()
    if len(cmd) == 1:
      cmd[0] = 'd.'+cmd[0]+'()'
    if len(cmd) == 2:
      cmd[0] = 'd.'+cmd[0]
      cmd[1] = '('+cmd[1]+')'
    cmd = ''.join(cmd)
    eval(cmd)
print(*d)
