#!/usr/bin/env python
    a = int(raw_input())
    A = set(raw_input().split())
    b = int(raw_input())
    B = set(raw_input().split())
    print(B.issuperset(A))
