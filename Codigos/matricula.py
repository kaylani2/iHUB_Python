import json

def escreverEmArquivoDeAlunos (nomeDoArquivo, novoAluno):
  with open (nomeDoArquivo, 'a') as meuArquivo:
    meuArquivo.write (novoAluno ['nome'] + '\n')
  return 0

def matricularAluno (novoAluno):
  with open (novoAluno ['nome'] + '.json', 'w') as meuArquivo:
    json.dump (novoAluno, meuArquivo)

def receberDadosAluno ():
  nome = input ('Insira o nome do aluno: ')
  cpf = input ('Insira o cpf do aluno: ')
  idade = int (input ('Insira a idade do aluno: '))
  matricula = 0
  aluno = {'nome': nome, 'matricula': matricula, 'idade': idade, 'cpf': cpf}
  return aluno

def listarTurma (nomeDoArquivo):
  turma = []
  with open (nomeDoArquivo, 'r') as meuArquivo:
    turma = meuArquivo.readlines ()
    #turma.insert (len (turma), meuArquivo.readline ())

  for aluno in turma:
    print (aluno.strip ())

def ordenarTurma (nomeDoArquivo):
  turma = []
  with open (nomeDoArquivo, 'r') as meuArquivo:
    turma = meuArquivo.readlines ()

  turma.sort ()
  with open (nomeDoArquivo, 'w') as meuArquivo:
    for aluno in turma:
      meuArquivo.write (aluno)


nomeDoArquivo = 'turma.txt'
ordenarTurma (nomeDoArquivo)
sair = False
listarTurma (nomeDoArquivo)
resposta = int (input ('Digite 0 para sair. Digite 1 para continuar.'))
if (resposta == 0):
  sair = True
while (sair == False):
  novoAluno = receberDadosAluno ()
  escreverEmArquivoDeAlunos (nomeDoArquivo, novoAluno)
  matricularAluno (novoAluno)
  resposta = int (input ('Digite 0 para sair. Digite 1 para continuar.'))
  if (resposta == 0):
    sair = True
