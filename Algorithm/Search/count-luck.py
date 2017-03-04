#!/usr/bin/env python
import re
import copy

def try_path(matrice,M,maxguess,curguess):
 
  # Max guess exceeded, exit
  if curguess > maxguess:
    return False
  
  # exit if position is the exit, and number of guess is correct
  if (matrice[M[0]][M[1]] == '*') and (curguess == maxguess) :
    #print 'Exit found !'
    return True

  elif matrice[M[0]][M[1]] == '*':
    return False

  # copy matrice and add M
  else:
    copymatrice = copy.deepcopy(matrice)
    ajout_arbre(copymatrice,M)
    # get position available around 
    slots=free_slot(copymatrice,M)
    # More than 1 position available, we add 1
    if len(slots) > 1:
      curguess+=1
  
    # for every position, try recursively
    for slot in slots:
      if (try_path(copymatrice,slot,maxguess,curguess)):
        return True
  return False

def ajout_arbre(liste,M):
  liste[M[0]][M[1]] = 'M'

def free_slot(liste,M):
  slots=list()
  # M is current position
  if len(liste) <= 2:
    startx=0
  else:
    startx=-1
  if len(liste[0]) <= 2:
    starty=0
  else:
    starty=-1
  for i in xrange(startx,2):
      x,y=M[0]+i,M[1]
      if (x >= len(liste)) or (x <= -1):
	continue
      elif liste[x][y] == '*':
        slots.append([x,y])
      elif liste[x][y] == '.':
        slots.append([x,y])
  for j in xrange(starty,2):
      x,y=M[0],M[1]+j
      if (y >= len(liste[0])) or (y <= -1):
        continue
      elif liste[x][y] == '*':
        slots.append([x,y])
      elif liste[x][y] == '.':
        slots.append([x,y])
  return slots


def pos_M(liste):
  for x,tab in enumerate(liste):
    for y,content in enumerate(tab):
      if content == 'M':
        return([x,y])

def affiche(liste):
  for line in liste:
    print line

if __name__ == '__main__':
  cases = int(raw_input())
  plateau = [] 
  maxguess = []
  for _ in range(cases):
    matrice_size = (map(int,raw_input().split()))
    case = []
    for _ in xrange(matrice_size[0]):
      line = raw_input()
      case.append(re.findall('.' ,line))
    maxguess.append(int(raw_input()))
    plateau.append(case)
  for j,plato in enumerate(plateau): 
    if try_path(plato,pos_M(plato),maxguess[j],0):
      print 'Impressed'
    else:
      print 'Oops!' 
