#!/usr/bin/env python3

a = input().split(' ')
i,j,k = [int(n) for n in a]
count = 0
for val in range(i,j):
    val_r = str(val)[::-1]
    if val_r[0] == "0":
        val_r = val_r[1:]
    val_r = int(val_r)
    if (val-val_r) % k == 0:
        count+=1
print(count)
