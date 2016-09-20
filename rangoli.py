import string

def recu(width,limit,indice,gap,reverse):
  if gap == limit:
    return
  line=str()
  gap_cpt=gap
  while gap_cpt > 0:
     line += string.ascii_lowercase[indice+gap_cpt]+'-'
     gap_cpt-=1

  line += string.ascii_lowercase[indice]

  for i in range(1,gap+1):
     line+= '-'+string.ascii_lowercase[indice+i]
  
  print(line.center(width,'-'))
  if not reverse:
    recu(width,limit,indice-1,gap+1,False)
  else:
    recu(width,limit,indice+1,gap-1,True)

num = input()
width=((num*2)-1)+((num-1)*2)
recu(width,num,num-1,0,False)
recu(width,-1,1,num-2,True)
