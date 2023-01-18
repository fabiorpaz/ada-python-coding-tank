'''
Faça um programa que leia a validade das informações:
Idade: entre 0 e 150;
Salário: maior que 0;
Sexo: M, F ou Outro;
O programa deve imprimir uma mensagem de erro para cada informação inválida.
'''
idade = int(input('informe qual a idade: '))
if 0 <idade> 150:
  print('idade invalida')
else:
  print(f'a idade é {idade}')
salario = float(input('informe qual o valor de salário: '))
if salario <= 0:
  print('salario invalido')
else:
  print(f'o salario é {salario}')
sexo = input('informe qual o sexo: ')
if sexo!= 'M' and 'F' and 'Outro':
  print('informação invalida')
else:
  print(f'seu sexo é {sexo}')