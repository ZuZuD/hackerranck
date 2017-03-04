#!/usr/bin/env python
from copy import copy

def swap(li,back,forw):
  # swap 2 elements in the list
  temp=li.pop(back)
  li.insert(forw,temp)
  temp=li.pop(forw-1)
  li.insert(back,temp)

def reverse(li,back,forw):
  # reverse a portion of list and insert it in the list
  temp=[]
  for pos in range(back,forw):
    temp.append(li[pos])
  temp.reverse()
  # delete range in list
  del li[back:forw]
  # add the new range 
  li[back:back]=temp

def sortederrors(li):
  # return errors position in list not sorted
  error = []
  last = -1
  for pos,elt in enumerate(li):
    if elt < last:
      error.append(pos)
    last = elt
  else:
    return error

def issorted(li):
  # test if list is sorted ascending
  last = -1
  for elt in li:
    if elt < last:
      return False
    last = elt
  return True

def isswappable(li,error):
  # cannot swap more than 2 errors
  if len(error) > 2:
    return False

  licp = copy(li)
  # one error, swap with previous element
  if len(error) == 1:
    swap(licp,error[0]-1,error[0])
    if issorted(licp):
      error.insert(0,error[0]-1)
      return True
  else:
  # two errors, swap previous with last
    swap(licp,error[0]-1,error[-1])
    if issorted(licp):
      error[0]=error[0]-1
      return True
  return False

def isreversible(li,error):
  # no consecutives errors
  if error[-1]-error[0] != len(error)-1:
    return False
  licp = copy(li)
  # reverse the errors
  reverse(licp,error[0]-1,error[-1]+1)
  if issorted(licp):
    error.insert(0,error[0]-1)
    return True
  return False

if __name__ == '__main__':

  #li = [1,2,8,5,4,3,9]
  # Add 1 to every print. Condition : Index start at 1 and not 0.
  input()
  li = list(map(int,input().split()))
  error = sortederrors(li)

  if not error:
    print("yes")

  elif isswappable(li,error):
    print("yes \nswap {} {}".format(error[0]+1,error[-1]+1))

  elif isreversible(li,error):
    print("yes \nreverse {} {}".format(error[0]+1,error[-1]+1))
 
  else:
    print("no")
