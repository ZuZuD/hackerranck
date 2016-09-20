num_array=(raw_input())
array=[]
for number in range(int(num_array)):
  length=raw_input()
  array.append(map(int,raw_input().split()))

for tab in array:
  ptr=0
  if len(tab) == 1:
    print 'YES'
  for i in range(len(tab)/2):
     total1=0
     total1 = sum(tab[:len(tab)/2+ptr])
     total2=0
     total2 = sum(tab[len(tab)/2+ptr+1:])
     if (total1 == total2):
       print 'YES'
       break
     elif (i == len(tab)/2-1):
       print 'NO'
     else:
       if (total1<total2):
          ptr+=1
       else:
          ptr+=-1


