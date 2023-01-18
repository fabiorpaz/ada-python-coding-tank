'''
Como aluno, você resolveu criar um código que indique 
a situação final de uma disciplina da faculdade. Nesta faculdade, 
o aluno é aprovado se obtiver uma nota superior a 9,0 ou se o aluno tiver nota maior que 6,0 
e frequência maior que 75%. Desenvolva um código que apresente na tela a situação final do aluno
('aprovado' ou 'reprovado'). Considere que as entradas são:
nota_final: média de notas do aluno (varia de 0 a 10)
frequencia: frequência do aluno (varia de 0 a 1)
'''
nota_final = float(input('Insira a nota final: '))
frequencia = float(input('Insira a frequencia: '))

if (nota_final > 9.0) or (nota_final > 6 and frequencia > 0.75):
  print('Aprovado')
else:
  print('Reprovado')
