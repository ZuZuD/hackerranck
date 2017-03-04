#!/usr/bin/env python3
import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
total = [0,0]
for app in apple:
    if (a+app) >= s and (a+app) <= t:
        total[0]+=1
for ora in orange:
    if (b+ora) >= s and (b+ora) <= t:
        total[1]+=1
print("%i\n%i"%(total[0],total[1]))
