#!/usr/bin/env python3

def lookup(num,p1play):
  while num not in [0,1]:
    found = False
    for i in moves:
      if ((num - i) % 7 in [0,1]) and ((num - i) >= 0) and not found:
        num = num - i
        p1play = not p1play
        found = True
    while not found:
      for i in moves:
        for j in moves[::-1]:
          if ((num - i) % j in [0,1]) and ((num - i) >= 0) and not found:
            num = num - i
            p1play = not p1play
            found = True
  return not p1play

lines = input()
moves = [2,3,5]
games = [int(input()) for _ in range(0,int(lines))]
for game in games:
  p1 = []
  p2 = []
  if lookup(game,True):
    print("First")
  else:
    print("Second")
