#!/usr/bin/env python

def sort_num(func):
  def wrapper(*args):
      return func(sorted(*args))
  return wrapper

@sort_num
def print_num(mylist):
  print "\n".join(["+91 {} {}".format(item[-10:-5],item[-5:]) for item in mylist])

size=input()
tab=[raw_input()[-10:] for j in range(size)]
print_num(tab)
