import json

with open ('exemplo.txt', 'r') as myFile:
  pessoa = json.load (myFile)
  print (type (pessoa))
  print (pessoa)
  print (pessoa ['nome'])
  pessoa ['nome'] = 'ok'

  with open ('novo.json', 'w') as myOtherFile:
    json.dump (pessoa, myOtherFile)


numeroDeAlunos = 10
for indiceAlunos in range (numeroDeAlunos):
  idade = indiceAlunos
