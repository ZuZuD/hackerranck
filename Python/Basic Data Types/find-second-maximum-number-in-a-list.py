#!/usr/bin/env python
num = raw_input()
lis = map(int, raw_input().split())
print sorted(list(set(lis)))[-2]
