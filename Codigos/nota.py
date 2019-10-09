#faltas > 25% --> REPROVADO POR FALTA
#  media >= 7 --> APROVADO DIRETO
#  3 <= media < 7 --> FAZER PROVA FINAL
#  3 > media --> REPROVADO DIRETO

nota1 = float (input ('Nota 1: '))
nota2 = float (input ('Nota 2: '))
presenca = int (input ('Indice de faltas: '))

media = (nota1+nota2)/2.0

if (presenca < 25):
  print ('Reprovado por faltas.')
else:
  if (media >= 7.0):
    print ('Aprovado direto.') 
  elif (media >= 3):
    print ('Fazer prova final.') 
  else:
    print ('Reprovado.')
