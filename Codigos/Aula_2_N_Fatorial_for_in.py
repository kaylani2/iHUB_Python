## Autora: Adriane

numero = int (input ('Fator N. '))
fatorial = 1

for contador in range (numero):
    numeroAtual = numero - contador 
    fatorial = fatorial * numeroAtual
print ('Fatorial:', fatorial)
