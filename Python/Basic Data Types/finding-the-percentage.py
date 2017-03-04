#!/usr/bin/env python
num = int(raw_input())
dict = {}
for i in range(0, num):
    line = raw_input()
        name = line.split()[0]
            dict[name] = line.split()[1], line.split()[2], line.split()[3]
            ans = str(raw_input())
            total = 0
            for i in dict[ans]:
                total = total + (float(i))
                print format(total / 3, '.2f')
