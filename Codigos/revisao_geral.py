def ordenarLista (lista):
  if (len (lista) == 0):
    return 1
  for i in range (len (lista) - 1):
    for j in range (len (lista) - 1):
      if (lista [j] > lista [j + 1]):
        auxiliar = lista [j]
        lista [j] = lista [j + 1]
        lista [j + 1] = auxiliar
        #lista [j], lista [j + 1] = lista [j + 1], lista [j]

  return 0

def potenciaDeDois (x):
  x = x**2
  return x

lista = []
for elemento in (lista):
  print (elemento)

print ()
print ()
ordenarLista (lista)
for elemento in (lista):
  print (elemento)


y = 3
print (y)
potenciaDeDois (y)
print (y)
