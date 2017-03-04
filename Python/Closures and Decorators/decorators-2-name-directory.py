#!/usr/bin/env python

def sort_name(func):
  def wrapper(*args):
      return [func(name) for name in sorted(*args, key=lambda x:x[2])]
  return wrapper

@sort_name
def print_name(mylist):
  return ("Mr. " if mylist[3] == "M" else "Ms. ") + mylist[0] + " " + mylist[1]

size=input()
name=[raw_input().split() for j in range(size)]
print  ('\n').join(print_name(name))
