'''
Faça um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e). 
Sabendo a resposta certa, o programa deve receber a opção do usuário 
e informar a letra que o usuário marcou e se a resposta está certa ou errada.
Para este problema, considere duas variáveis. A variável resposta_certa armazenará uma string
com a opção que deve ser correta, e resposta_atual será utilizada para "coletar" 
a alternativa inserida pelo usuário (usando o input). 
Caso a resposta seja incorreta, o programa deve gerar uma resposta do tipo:
Errada (você escolheu 'a', mas a resposta correta é 'b').
'''
print('por favor, informe qual a opção correta da questão entre as letras: \n')
print('a\n')
print('b\n')
print('c\n')
print('d\n')
print('e\n')
resposta_certa = 'b'
resposta_atual = input()

if resposta_atual == resposta_certa:
  print('parabéns, você acertou!')
else:
  print(f'\nvocê escolheu {resposta_atual}, mas a resposta correta é {resposta_certa}')