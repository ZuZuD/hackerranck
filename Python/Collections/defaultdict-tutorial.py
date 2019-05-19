#!/usr/bin/env python3
'''
URL: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem


Sample Input

5 2
a
a
b
a
b
a
b

Sample Output

1 2 4
3 5

Explanation

'a' appeared 3
times in positions 1,2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print -1.
'''

from collections import defaultdict
da = defaultdict(list)
n,m = [int(v) for v in input().strip().split()]

for i in range (n):
    da[input()].append(i+1)

for _ in range(m):
    b = input()
    print(*da.get(b,[-1]), sep=' ')
