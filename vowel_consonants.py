import string 
def try_word(word):
  score,j=0,1
  while j < len(word):
    i=0
    motif = word[:j]
    print 'motif',motif
    while i < len(word):
      print word[i:len(motif)+i]
      if word[i:len(motif)+i] == motif:
        score+=1
        print '+1'
      i+=1
    j+=1
  return score

vow = map(str,"A,E,I,O,U".split(','))
con = list() 
for letter in string.ascii_uppercase:
   if letter not in vow:
     con.append(letter)
word = raw_input()
cpt,i = 0,0
vow_lst=list()
while i < len(word):
  letter = word[i]
  if letter in vow and letter not in vow_lst:
    cpt+= try_word(word[i:])
    cpt+=1
    vow_lst.append(letter)
  i+=1
kevin = cpt
cpt,i = 0,0
con_lst=list()
while i < len(word):
  letter = word[i]
  if letter in con and letter not in con_lst:
    cpt+= try_word(word[i:])
    cpt+=1
    con_lst.append(letter)
  i+=1
stuart=cpt
if stuart > kevin:
  print 'Stuart',stuart
elif stuart < kevin:
  print 'Kevin',kevin
else:
  print 'Draw'
