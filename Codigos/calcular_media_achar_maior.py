def calcularMedia (listaDeNotas):
  acumulador = 0.0
  for nota in listaDeNotas:
    acumulador += nota
  return acumulador/len (listaDeNotas)


def acharMaior (lista):
  maiorAtual = lista [0]
  for elemento in lista:
    if (maiorAtual < elemento):
      maiorAtual = elemento
  return maiorAtual


lista = [10, 2, 12, 89]

maior = acharMaior (lista)
print (maior)
