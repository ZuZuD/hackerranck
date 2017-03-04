#!/usr/bin/env python

group_size = input()
rooms = map(int, raw_input().split())
nums = Counter(rooms)
print min(nums, key=nums.get)
