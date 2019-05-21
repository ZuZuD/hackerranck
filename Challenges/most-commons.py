#!/usr/bin/env python3

'''
URL: https://www.hackerrank.com/challenges/most-commons


Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde

Sample Output 0

b 3
a 2
c 2

Explanation 0

aabbbccde

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string S has at least 3 distinct characters. 

'''
from collections import Counter

c = Counter(sorted(input()))
[ print(k,v) for k,v in c.most_common(3) ]
