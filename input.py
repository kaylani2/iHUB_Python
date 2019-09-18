## Autor: Kaylani Bochie

## Primeira maneira:
print ('Digite algo: ' )
minhaString = input ()
print ('A string digitada foi: ', minhaString)
## Note que o print pula uma linha automaticamente.

## Para nao pular uma linha:
print ('Digite algo: ', end = '')
minhaString = input ()
print ('A string digitada foi: ', minhaString)


## Segunda maneira:
minhaString = input ('Digite algo: ' )
print ('A string digitada foi: ', minhaString)
## Note que o input nao pula uma linha automaticamente.


## Para ler numeros:
meuNumero = int (input ('Digite um numero: ' ))
print ('O programa teria dado erro se voce nao tivesse inserido um numero')
print ('O numero digitado + 10 foi: ', str (meuNumero + 10))
## Note o type casting na entrada e na saida.
