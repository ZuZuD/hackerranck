import itertools
# input : HACK 2 
# ca trie la sortie par 2 characteres
A = map(str,raw_input().split())
liste = str()
for i in range(int(A[1])+1):
  for elt in list(itertools.combinations(sorted(A[0]),i)):
    print("".join(elt))
