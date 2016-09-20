import itertools
# input : HACK 2 
# ca trie la sortie par 2 characteres
A = map(str,raw_input().split())
liste = str()
for elt in list(itertools.permutations(sorted(A[0]),int(A[1]))):
  print("".join(elt))
