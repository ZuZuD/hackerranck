#!/usr/bin/env python3

'''
URL: https://www.hackerrank.com/challenges/py-collections-ordereddict/


Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

Explanation

BANANA FRIES: Quantity bought: 1
, Price: 12
Net Price: 12
POTATO CHIPS: Quantity bought: 2, Price: 30
Net Price: 60 
APPLE JUICE: Quantity bought: 2, Price: 10
Net Price: 20
CANDY: Quantity bought:4 , Price: 5
Net Price: 20

'''

from collections import OrderedDict
ordered_dict = OrderedDict()

for _ in range(int(input())):
  order = input().split()
  candy = " ".join(order[:-1])
  ordered_dict[candy] = ordered_dict.get(candy, 0) + int(order[-1])
[print(k,v) for k,v in ordered_dict.items()]
