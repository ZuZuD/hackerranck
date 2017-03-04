#!/usr/bin/env python
row = input()
for i in range(row):
    div = raw_input().split()
    try:
        print int(div[0]) / int(div[1])
    except (ZeroDivisionError, ValueError) as e:
        print "Error Code: {}".format(e)
