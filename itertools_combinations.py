from itertools import combinations
import decimal

num = input()
li = raw_input()
#li = "a a u u y e d"
lis = [i for i in combinations([j for j in (li.split(" "))],num)]
count = 0
print lis
for tup in lis:
  if 'a' in tup:
    count +=1
print count
output = decimal.Decimal(float(count)/float(len(lis)))
print(round(output,4))
