try:
  handle = open ('nome', 'r')
  m = int (input ('Digite sua massa: '))
except (ValueError, FileNotFoundError) as error:
  print ('Nao foi um inteiro')
  print (dir (error))
else:
  print ('Peso na terra: ', m*9.8)
  print ('Peso em marte: ', m*3.7)
finally:
  print ('Sempre sera executado')

