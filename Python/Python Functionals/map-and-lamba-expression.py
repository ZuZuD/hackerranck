#!/usr/bin/env python3
def fibonacci(limit):
    fib = []
    for i in range(limit):
        if (i < 2):
            fib.append(i)
        else:
            fib.append(fib[i - 1] + fib[i - 2])
    return fib

fib = (fibonacci(int(input())))
print([i ** 3 for i in fib])
