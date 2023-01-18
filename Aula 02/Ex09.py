#Faça um programa que leia 3 números e informe o maior deles.
val1 = float(input('Insira o primeiro valor: '))
val2 = float(input('Insira o segundo valor: '))
val3 = float(input('Insira o terceiro valor: '))

if (val1 >= val2) and (val1 >= val3):
  print(f'Maior valor é {val1}')
elif (val2 >= val3) and (val2 >= val1):
  print(f'Maior valor é {val2}')
else:
  print(f'Maior valor é {val3}')