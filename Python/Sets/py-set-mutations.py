#!/usr/bin/env python
s = set(map(int, raw_input().split()))
m = input()
for i in range(m):
    cmd = map(str, raw_input().split())
    lis = set(map(int, raw_input().split()))
    eval("s." + cmd[0] + "(lis)")
print sum(s)
