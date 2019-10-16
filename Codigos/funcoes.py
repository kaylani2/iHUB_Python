## Definicao da funcao
def calcularFatorial (numero):
  ## Tratamento de erro rudimentar
  if (numero < 0):
    return numero

  fatorial = 1
  for contador in range (1, (numero + 1)):
    fatorial = fatorial * contador

  return fatorial


## Definicao da funcao
def calcularCombinacao (n, p):
  return calcularFatorial (n)/(calcularFatorial (p)*calcularFatorial (n - p))


## Chamada da funcao
print (calcularCombinacao (10, 2))
