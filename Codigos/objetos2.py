class Veiculo:

  numeroDeVeiculos = 0

  def __init__ (self, cor, marca):
    self.__cor = cor
    self.marca = marca
    Veiculo.numeroDeVeiculos += 1
    print ('Veiculo da cor', self.__cor, 'criado.')
    print ('Quantidade de veiculos:', Veiculo.numeroDeVeiculos)

  def getCor (self):
    return self.__cor

  def imprimirInformacoes (self):
    print (self.__cor, self.marca)

  def andar (self, metros):
    print ('Andei', metros, 'metros.')

  def __del__ (self):
    print ('Veiculo da cor', self.__cor, 'destruido.')
    Veiculo.numeroDeVeiculos -= 1
    print ('Quantidade de veiculos:', Veiculo.numeroDeVeiculos)

  @classmethod
  def getNumeroDeVeiculos (cls):
    return cls.numeroDeVeiculos


class Barco (Veiculo):
  def andar (self, distancia):
    print ('Naveguei', distancia, 'metros.')

  def socobrar (self):
    print ('Socobrei.')



def f ():
  x = Veiculo ('rosa', 'qwe')

#veiculoDaZei = Veiculo ('preto', 'fiat')
#meuVeiculo.andar (10)
#veiculoDaZei.imprimirInformacoes ()



meuVeiculo = Veiculo ('vermelho', 'honda')
seuVeiculo = Veiculo ('vermelho', 'honda')
meuVeiculo.imprimirInformacoes ()
for _ in range (5):
  f ()
#print (dir (meuVeiculo))
#meuVeiculo.__cor = 10
meuVeiculo.imprimirInformacoes ()
#print (dir (meuVeiculo))
print ('\n\n\n\n')
print (meuVeiculo.getCor ())
print (Veiculo.getNumeroDeVeiculos ())


meuBarco = Barco ('branco', 'yamaha')
meuBarco.andar (10)
print (dir (meuBarco))
print (type (meuBarco))
