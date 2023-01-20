'''
Faça um programa que mostre o fatorial de um número digitado.

Exemplo

número digitado: 5
resultado esperado: 120
OBS1: Considere que 0! é igual a 1.

OBS2: Não existe fatorial de um número negativo. 
Neste caso, se o usuário digitar um número negativo, o programa deve escrever 
"Não existe fatorial de um número negativo!"
'''
n = int(input('Insira o número: '))
soma = 1
if n < 0:
  print('Não é possível realizar a operação')
else:
  for i in range(2,n+1):
    soma *= i

print(soma) 