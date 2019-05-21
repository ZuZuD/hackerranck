#!/usr/bin/env python3

'''
URL: https://www.hackerrank.com/challenges/piling-up/

Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output

Yes
No

Explanation

In the first test case, pick in this order: left - 4 , right - 4 , left - 3, right - 3, left - 2, right - 1.
In the second test case, no order gives an appropriate arrangement of vertical cubes. will always come after either or .

'''


from collections import deque

d = deque()
tests = int(input())

for _ in range(tests):
    length = int(input())
    d.extend([int(i) for i in input().split()])
    li = []
    straight = True
    for i in range(length):
        if d[0] >= d[-1]:
            highest = d.popleft()
        else:
            highest = d.pop()
        if len(li) == 0: 
            li.append(highest)
        elif li[-1] >= highest:
            li.append(highest)
        else: 
            straight = False
            break
    if straight:
        print('Yes')
    else:
        print('No')
