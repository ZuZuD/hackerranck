#!/usr/bin/env python3
def research(x,i,k):
      if (i+k) in x:
          return k
      else:
          research(x,i,k-1)
            
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]
x.sort()
  
ant = []
i = 0
  
while i < len(x):
  myval = x[i]
  while (i < len(x)-1) and (k >= x[i+1]-myval):
    i += 1
  ant.append(x[i])
  myval = x[i]
  while (i < len(x)-1) and (k >= x[i+1]-myval):
    i += 1
  i += 1
print(len(ant))
