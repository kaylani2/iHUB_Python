## Autora: Adriane

numeroDeNotas = int (input ('Numero de notas: '))
acumuladorDeNotas = 0.0

for contador in range (numeroDeNotas):
    notaAtual = float (input ('Nota: '))
    acumuladorDeNotas = acumuladorDeNotas + notaAtual

mediaDeNotas = acumuladorDeNotas / numeroDeNotas
print ('Média:', mediaDeNotas)
