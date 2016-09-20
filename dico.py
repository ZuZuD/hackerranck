import os   

import re

dict1 = {}
dict1['Dino1'] = "Bidep","1.80"
dict1['Dino2'] = "Bidep","1.40"
dict1['Dino3'] = "Bidepal","1.30"

dict2 = {}
for enum,dino in enumerate(dict1.keys()):
    dict2[dino] = enum+10
print dict2

# dict.values() => les valeurs
# dict.keys()   => les cles
# dict.items()  => les 2 (values + keys)

for dino,info in dict1.items():
    print("Le dino {} de taille {} est de type {}.".format(dino, info[1], info[0]))

    if (float(info[1])) >= 1.40:
      dict2[dino] = 'fast'
    else:
        dict2[dino] = 'slow'
print dict2
