def cut_float(number):

  if type(number) is not float:
    raise TypeError("Le parametre nest pas un flottant")
  number=str(number)
  entier,flottant=number.split(".")
  print(",".join([entier,flottant[:3]]))

if __name__ == '__main__':
  cut_float(3.999998)
