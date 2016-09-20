from itertools import groupby
# input 11111442 5,1 2,4 et 1,2
print ' '.join([str((len(list(y)), int(x))) for x,y in groupby(raw_input())])
