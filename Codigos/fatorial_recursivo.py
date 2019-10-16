def contarAteDez (inicio):
  if (inicio > 10):
    return inicio 

  print (inicio)
  inicio += 1
  contarAteDez (inicio)

def calcularFatorialRecursivo (n):
  if (n == 1):
    return 1
  return n*calcularFatorialRecursivo (n - 1)

