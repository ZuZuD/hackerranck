import re
import pdb
import copy

def try_path(matrice,M,maxguess,curguess):
 
  pdb.set_trace() 
  # on sort
  if curguess > maxguess:
    #print 'Max guess exceeded'
    return False
  
  # on sort si la position est la sortie et le nombre de guess est exacte
  if (matrice[M[0]][M[1]] == '*') and (curguess == maxguess) :
    #print 'Exit found !'
    return True

  # sinon on return false
  elif matrice[M[0]][M[1]] == '*':
    return False

  # sinon on copie la matrice et on ajoute un M
  else:
    copymatrice = copy.deepcopy(matrice)
    ajout_arbre(copymatrice,M)
    # on recupere les positions autour disponibles
    slots=free_slot(copymatrice,M)
    # si il y a plus de 1 pos, on incremente le compteur
    if len(slots) > 1:
      curguess+=1
  
    # pour chaque position, recursive
    for slot in slots:
      #print 'cur guess is',curguess
      #print 'max guess is',maxguess
      if (try_path(copymatrice,slot,maxguess,curguess)):
        return True
  return False

def ajout_arbre(liste,M):
  liste[M[0]][M[1]] = 'M'

def free_slot(liste,M):
  slots=list()
  #print 'position actuelle :',M
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
  #print 'SLOT',slots
  return slots


def pos_M(liste):
  for x,tab in enumerate(liste):
    for y,content in enumerate(tab):
      if content == 'M':
        return([x,y])

def affiche(liste):
  for line in liste:
    print(line)

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
      print('Impressed')
    else:
      print('Oops!')
