#!/usr/bin/env python
num = input()
L = list()
for _ in xrange(num):
    line = raw_input().split(' ')
    cmd = line[0]
    arg = line[1:]
    if cmd != "print":
        cmd += "(" + ",".join(arg) + ")"
        eval("L." + cmd)
    else:
        print L
