'''
Imagine que você está implementando um sistema para verificar 
se os alunos de uma turma estudantil passaram na disciplina ou não.
Para isso solicite que o usuário insira as notas das 4 provas realizadas por um estudante e calcule
a média. Após isso, emita uma resposta booleana (True ou False) se o estudante passou na disciplina
pensando que a média mínima para aprovação é que seja pelo menos 7.
'''
nota1 = float(input('Insira a nota 1: '))
nota2 = float(input('Insira a nota 2: '))
nota3 = float(input('Insira a nota 3: '))
nota4 = float(input('Insira a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f'A pessoa foi aprovada? {media >= 7}')