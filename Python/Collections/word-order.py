#!/usr/bin/env python3
'''
URL: https://www.hackerrank.com/challenges/word-order/problem

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1

Explanation

There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
'''

import collections

di = collections.OrderedDict()
length = int(input())
words = [str(input()) for _ in range(length)]
print(len(set(words)))
ref = words[0]
for word in words:
    di[word] = di.get(word, 0)+1
print(*[v for v in di.values()])
