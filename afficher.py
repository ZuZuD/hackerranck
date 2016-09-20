def afficher_string(*parameters, sep=' ', fin='\n'):

  # Modify tuple to list
  parameters=list(parameters)

  for i,parameter in enumerate(parameters):
     parameters[i]=str(parameter)
     print (parameters[i])
  chaine=sep.join(parameters)
  chaine += fin
  print(chaine, end='')

if __name__ == '__main__':
  afficher_string('toto', 'est', 'un', 'salop')
