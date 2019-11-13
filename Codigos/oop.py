class Passaro:
  def __init__ (self, nome):
    print ('nasceu')
    self.nome = nome

  def cantar (self):
    print ('meu nome eh', self.nome)

pablo = Passaro ('pablo')
marie = Passaro ('marie')

pablo.nome
pablo.cantar ()
pablo.nome = 'ok'
pablo.cantar ()
print (getattr (pablo, 'nome'))
