'''
Faça um script que peça para o usuário digitar a idade, 
o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.
a. Idade: entre 0 e 150
b. Salário: maior que 0
c. Gênero: M, F ou Outro

Por último imprima os dados recebidos do usuário.
'''
idade = int(input('Insira a tua idade:'))
while (idade < 0) or (idade > 150):
  idade = int(input('Insira a tua idade: '))

salario = int(input('Insira o teu salário: '))
while (salario < 0):
  salario = int(input('Insira o teu salário: '))

sexo = input('Insira o teu sexo: ')
while sexo not in ['M','F','Outro']:
  sexo = input('Insira o teu sexo: ')