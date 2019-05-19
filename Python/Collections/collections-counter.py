#!/usr/bin/env python3

'''
URL: https://www.hackerrank.com/challenges/collections-counter/problem


Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200

Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned = 55 + 45 + 40 + 60 = 200$
'''

from collections import Counter

num_shoes = input()
shoes =[int(i) for i in input().split()]

num_customer = int(input())
customer_req = [[int(i) for i in input().split()] for _ in range(num_customer)]

shoes_avail = Counter(shoes)
money = 0

for req in customer_req:
  if req[0] in shoes_avail.keys():
    if shoes_avail[req[0]] > 0:
      shoes_avail[req[0]] -= 1
      money += req[1]
print(money)
