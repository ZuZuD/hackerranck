#!/usr/bin/env python3

N, M = (int(i) for i in input().split())
coins = {int(i) for i in input().split()}
results = [1] + [0] * 254

def poly_mult(arr1, arr2):
    '''Multiplying 2 polynomials of 255 coefficients'''
    arr_prod = [0]*255
    for i in range(255):
        for j in range(i+1):
            arr_prod[i] += arr1[j]*arr2[i-j]
    return arr_prod
    
for c in coins:
    coin_arr = [1 if pos % c == 0 else 0 for pos in range(255)]
    results = poly_mult(results, coin_arr)
        
print(results[N])
