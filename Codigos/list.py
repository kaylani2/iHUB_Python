nota1 = 10
nota2 = 3

notas = [10, 3, 5, 11, 8] + [1, 5]

for indiceNotas in range (len (notas)):
  print (notas [indiceNotas])

for nota in notas:
  print (nota)

print (notas)
notas.insert (0, 1099999)
#notas.sort (reverse=True)
print (notas)

'''
matrizQualquer = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

print (matrizQualquer)
print (matrizQualquer [2][1])

for indiceLinhas in range (len (matrizQualquer)):
  for indiceColunas in range (len (matrizQualquer[0])):
    print (matrizQualquer [indiceLinhas][indiceColunas], end = ' ')
  print ()
'''


umaTupla = (10, 10, 5)
#umaTupla [0] = 1
print (type (umaTupla))
print (umaTupla [0])

nome = input ('Digite o nome:')
pessoa = {'nome': nome, 'idade': 24, 'cpf': '149...', 'bairros': ['bangu', 'pechincha']}
print (pessoa ['nome'])
print (pessoa ['bairros'][0])
