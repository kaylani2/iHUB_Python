numeroDeNotas = int (input ('Numero de notas: '))

acumuladorDeNotas = 0.0
for contadorDeNotas in range (numeroDeNotas):
  notaAtual = int (input ('Digite a nota ' + str (contadorDeNotas + 1)))
  acumuladorDeNotas = acumuladorDeNotas + notaAtual

mediaDasNotas = acumuladorDeNotas / numeroDeNotas
print ('Media:', mediaDasNotas)
