'''
Faça um programa que peça um número e mostre se ele é positivo ou negativo.
'''
n = float(input("informe qual o numero: "))
if n>=0:
  print('seu numéro é positivo')
elif n == 0:
  print('O número é neutro')
else:
  print('seu numéro é negativo')