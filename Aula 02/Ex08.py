'''
Um produto vai sofrer aumento de acordo com a Tabela 1 abaixo.
Faça um programa que peça para o usuário digitar o valor do produto de acordo com o preço antigo
e escreva uma das mensagens da Tabela 2, de acordo com o preço reajustado:
8. Um produto vai sofrer aumento de acordo com a Tabela 1 abaixo. Faça um programa que peça para o usuário digitar o valor do produto de acordo 
com o preço antigo e escreva uma das mensagens da Tabela 2, de acordo com o preço reajustado:

Tabela 1

| Preço Antigo         | % de aumento |
|----------------------|--------------|
| Até 50 reais         | 5%           |
| Entre 50 e 100 reais | 10%          |
| De 100 a 150 reais   | 13%          |
| Acima de 150 reais   | 15%          |

Tabela 2

| Preço Novo            | Mensagem   |
|-----------------------|------------|
| Até 80 reais          | Barato     |
| Entre 80 e 115 reais  | Razoável   |
| Entre 115 e 150 reais | Normal     |
| Entre 150 e 170 reais | Caro       |
| Acima de 170 reais    | Muito Caro |
'''
preco = float(input('Insira o valor do preço: '))

# Etapa 1 - Mudança de preço
if preco <= 50:
  novo_preco = 1.05*preco
elif preco <= 100:
  novo_preco = 1.10*preco 
elif preco <= 150:
  novo_preco = 1.13*preco
else:
  novo_preco = 1.15*preco 

# Etapa 2 - Rotular o novo preço
if novo_preco <= 80: 
  print('Barato')
elif novo_preco <= 115:
  print('Razoável')
elif novo_preco <= 150:
  print('Normal')
elif novo_preco <= 170:
  print('Caro')
else:
  print('Muito caro')