#muito quente: temperatura > 40
#quente: 25 < temperatura <= 40
#agradavel: 20 < temperatura <= 25
#frio: 10 < temperatura <= 20
#muito frio: temperatura <= 10

temperatura = int (input ('Digite a temperatura. '))

if (temperatura > 40):
    print ('Muito quente.')
elif (temperatura > 25):
    print ('Quente.')
elif (temperatura > 20):
    print ('Agradavel.')
elif (temperatura > 10):
    print ('Frio.')
else:
    print ('Muito frio.')
