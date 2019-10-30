def somarNotasAluno (aluno):
  somaDasNotas = 0
  for nota in aluno ['notas']:
    somaDasNotas += nota
  return somaDasNotas

def calcularMediaDaTurma (turma):
  numeroDeNotas = len (turma) * len (turma [0]['notas'])
  somaDasNotas = 0.0
  for aluno in turma:
    somaDasNotas += somarNotasAluno (aluno)
  return somaDasNotas/numeroDeNotas



aluno = {'nome': 'ok', 'registro': 10, 'notas' : [0, 10, 5]}
alunoA = {'nome': 'ok', 'registro': 10, 'notas' : [10, 10, 5]}
alunoB = {'nome': 'ok', 'registro': 10, 'notas' : [0, 10, 5]}

lista = [aluno, alunoA]#, alunoB]

print (somarNotasAluno (alunoA))
print (calcularMediaDaTurma (lista))
