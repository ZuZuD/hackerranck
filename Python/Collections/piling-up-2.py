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
for t in range(int(input())):
    input()
    lst = [int(i) for i in  input().split()]
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i == l - 1 else "No")
