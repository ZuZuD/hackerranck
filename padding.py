print('Entrez un nombre pour padding')
num=input()
for i in range(num):
  print('{:0<3}'.format(i))

print('padding dans lautre sens')
for i in range(num):
  print('{:0>3}'.format(i))
