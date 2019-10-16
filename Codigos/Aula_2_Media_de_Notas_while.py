## Autora: Adriane

numeroDeNotas = int (input ('Numero de notas: '))
acumuladorDeNotas = 0.0
contador = numeroDeNotas

while (contador != 0):
    notaAtual = float (input ('Nota: '))
    acumuladorDeNotas = acumuladorDeNotas + notaAtual
    contador = contador - 1

mediaDeNotas = acumuladorDeNotas / numeroDeNotas
print ('Média:', mediaDeNotas)
