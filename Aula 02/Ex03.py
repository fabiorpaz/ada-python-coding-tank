'''
Desenvolva um código que indique se um número x é divisível por y. 
Caso positivo, imprima na tela também qual é o resultado da divisão de x por y.
Lembrete: o número x é divisível por y se o resto da divisão de x por y é igual a zero.
'''
x = float(input('informe qual o primeiro numero: '))
y = float(input('inorme qual o segundo numero: '))

if x % y == 0:
  print(f'o resultado da divisão de {x} e {y} é {x/y}')
else:
  print ('o numéro escolhido não é divisível pelo outro')