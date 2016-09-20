array1= [48,1,2,1,15,20,10]
array2=[3,12,18,1,1,1,1,1,37]
array3=[20,1,15,1,1,1,2]
array=[array1,array2,array3]

for tab in array:
  ptr=0
  for _ in range(len(tab)/2):
     total1=0
     total1 = sum(tab[:len(tab)/2+ptr])
     total2=0
     total2 = sum(tab[len(tab)/2+ptr+1:])
     if (total1 == total2):
       print 'YES'
       print ' total1 :'+ str(total1) +' et total2:'+ str(total2)
       print tab
       break
     else:
       print 'NO'
       print ' total1 :'+ str(total1) +' et total2:'+ str(total2)
       print tab
       if (total1<total2):
          ptr+=1
       else:
          ptr+=-1


