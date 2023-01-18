'''
faça um programa que solicite ao usuário que insira seu ano de nascimento. 
Desconsiderando o mês do ano de nascimento, 
emita uma mensagem dizendo quantos anos ele possui.
'''
#Para automatizar a data atual, usamos a biblioteca datetime.
ano_atual = 2022
ano_nascimento = int(input('Indique o teu ano de nascimento:  '))

print(f'Você possui {ano_atual - ano_nascimento} anos')