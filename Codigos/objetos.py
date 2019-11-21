def f ():
  x = Veiculo (10, 10)
  print (x)

## Criar a classe
class Veiculo:

  ## Atributo de classe
  quantidadeDeVeiculos = 0

  ## Definir o construtor, inicializar atributos do objeto
  def __init__ (self, cor, preco):
    self.cor = cor
    self.preco = preco
    Veiculo.quantidadeDeVeiculos += 1
    print ('Veiculo criado.')

  ## Definir metodos
  def exibirInformacoes (self):
    print ('Quantidade de veiculos', self.quantidadeDeVeiculos, '. Cor:', self.cor, '. Preco:',
           self.preco)

  def andar (self, distancia):
    print ('Andei', distancia, 'metros.')

  def __del__ (self):
    Veiculo.quantidadeDeVeiculos -= 1
    print ('Adeus.')


  ## Note o uso do decorador
  @classmethod
  def exibirTipo (cls):
    print ('Tipo:', cls.quantidadeDeVeiculos)


class Carro (Veiculo):
  numeroDeRodas = 4

  def exibirInformacoes (self):
    Veiculo.exibirInformacoes (self)
    print ('Numero de rodas:', Carro.numeroDeRodas)

  def pagarPedagio (self):
    print ('Paguei 7 reais.')

class Moto (Veiculo):
  numeroDeRodas = 2

  def exibirInformacoes (self):
    Veiculo.exibirInformacoes (self)
    print ('Numero de rodas:', Moto.numeroDeRodas)

  def pagarPedagio (self):
    print ('Nao pago pedagio')



meuVeiculo = Veiculo ('preto', 2_000_000)
meuVeiculo.exibirInformacoes ()
meuVeiculo.andar (10)
print ('\n\n')

## Problema: Usuario da classe pode acessar o atributo diretamente
## NAO HA ENCAPSULACAO
## "Solucao": utilizar o atributo precedido por __
## Exemplo: self.__cor -> Impede que o atributo seja visto de fora
meuVeiculo.cor = 'laranja'
meuVeiculo.exibirInformacoes ()
meuVeiculo.cor = 10
print ('Cor acessada diretamente:', meuVeiculo.cor)
meuVeiculo.exibirInformacoes ()
print (dir (meuVeiculo))

for _ in range (10):
  meuOutroVeiculo = Veiculo ('preto', 2_000_000)
  meuOutroVeiculo.exibirInformacoes ()
  meuTerceiroVeiculo = Veiculo ('preto', 2_000_000)
  meuTerceiroVeiculo.exibirInformacoes ()


f ()
print ('Depois do loop')

#meuCarro = Carro ('preto', 4)
#meuCarro.pagarPedagio ()
#
#minhaMoto = Moto ('preto', 2)
#minhaMoto.pagarPedagio ()
#Veiculo.exibirTipo ()
#
#meuCarro.exibirInformacoes ()
#minhaMoto.exibirInformacoes ()

