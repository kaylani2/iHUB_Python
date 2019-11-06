def removerDuplicados (lista):
  listaNova = []
  for indiceFixo in range (len (lista)):
    for indiceVariavel in range (len (lista)):
      if ( (lista [indiceFixo] == lista [indiceVariavel]) and (indiceFixo != indiceVariavel) ):
        #lista.pop (indiceVariavel) ## Altera o comprimento da lista
        lista [indiceVariavel] = -1
        ## Marcar todos os elementos que devem ser removidos

  for elemento in lista:
    if (elemento != -1):
      listaNova.append (elemento)


  return listaNova

def removerDuplicadosRecursivo (lista):
  for indiceFixo in range (len (lista)):
    for indiceVariavel in range (len (lista)):
      if (lista [indiceFixo] == lista [indiceVariavel]) and (indiceFixo != indiceVariavel):
        lista.pop (indiceVariavel)
        return removerDuplicadosRecursivo (lista)

  return lista


lista = removerDuplicadosRecursivo (lista)
print (lista)
