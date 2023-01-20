'''
Faça um programa que imprima o maior número de uma lista,
sem usar o método max. Em seguida, usando o método max, 
faça um programa que imprima os três maiores números de uma lista
'''
lista = [5, 10, 500, 800, -1000]

maior = -10000
for i in lista:
  if i > maior:
    maior = i

print(f'Maior número da lista é {maior}')
