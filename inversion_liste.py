inventaire = [
  ('fraise', 3),
  ('meulon', 9),
  ('tartiflette', 12),
  ('tomatoe', 1),
]
print("Inventaire de base")
print(inventaire)
print("Inventaire inverse")
sorted_inventaire=[(nombre,miam) for miam,nombre in inventaire ]
print(sorted_inventaire)
sorted_inventaire.sort(reverse=True)
print("Inventaire trie decroissant")
print(sorted_inventaire)
