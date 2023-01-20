'''
Vamos fazer um jogo de adivinhação. Este jogo é feito para duas pessoas, 
e é jogado em duas etapas. Na primeira etapa, o primeiro jogador deve fornecer um número inteiro 
entre 0 e 500. O segundo jogador, sem saber este número, deve adivinhar até conseguir acertar, 
sendo contabilizado o número de tentativas até acertar o número. A cada adivinhação, 
o programa deve retornar se o número escolhido é maior ou menor do que o fornecido pelo primeiro jogador.
Na segunda etapa, o jogo é invertido (i.e. o segundo jogador fornece o número inteiro e o primeiro jogador deve adivinhá-lo). 
O vencedor deste jogo será a pessoa que conseguir, no final, adivinhar o número com o menor número de rodadas.
Crie um código que reproduza o jogo, mostrando na tela o vencedor da partida.
'''
p1 = int(input('Escolha o número entre 1 e 500: '))
while (p1 < 1) or (p1 > 500):
  p1 = int(input('Escolha o número entre 1 e 500: '))


p2_guess = int('Faça o teu primeiro chute: ')
p2_tries = 1 
while p2_guess != p1:
  if (p2_guess > p1):
    print('Você escolheu um número maior!')
  else:
    print('Você escolheu um número menor')
  p2_guess = int('Faça o teu próximo chute: ')
  p2_tries += 1

p2 = int(input('Escolha o número entre 1 e 500: '))
p1_guess = int('Faça o teu primeiro chute: ')
p1_tries = 1 
while p1_guess != p2:
  if (p1_guess > p2):
    print('Você escolheu um número maior!')
  else:
    print('Você escolheu um número menor')
  p1_guess = int('Faça o teu próximo chute: ')
  p1_tries += 1