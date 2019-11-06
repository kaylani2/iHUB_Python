def multiplicarMatrizes (A, B):
  linhasResultante = len (A)
  colunasResultante = len (B [0])
  colunasA = len (A [0])

  C = [[0 for x in range (colunasResultante)] for y in range (linhasResultante)]

  for i in range (linhasResultante):
    for j in range (colunasResultante):
      acumulador = 0
      for k in range (colunasA):
        acumulador += A [i][k] * B [k][j]
      C [i][j] = acumulador

  return C

A = [
    [1, 2],
    [3, 4]
    ]
B = [
    [1, 2, 3],
    [4, 5, 6]
    ]
print (multiplicarMatrizes (A, B))


### Agora com o numpy

import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 2, 3], [4, 5, 6]])
print (A.dot (B))
