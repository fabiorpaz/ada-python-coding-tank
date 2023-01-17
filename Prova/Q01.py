"""
Um jovem criou um jogo de cartas alternativo, chamado de Blackjack reverso. 
Neste jogo, desenvolvido para um total de 4 participadas, cada participante começa com a pontuação igual a 21 e,
conforme cada um vai recebendo uma carta a cada rodada, o valor desta é subtraído de sua pontuação total.

A última rodada acontecerá quando pelo menos uma pessoa obtiver a pontuação final negativa,
e a pessoa vencedora será aquela que obtiver a menor pontuação possível. 
Crie um código que reproduza o jogo e mostre na tela o índice da pessoa que ganhou o jogo.

Considere que as cartas estão armazenadas em uma variável do tipo list.

OBS: os valores das cartas variam de 1 a 10.

Exemplo de jogo:

cartas = [10, 5, 7, 8, 5, 3, 4, 3, 9, 8, 5, 10, 7, 6, 5]

1ª rodada

Usuário 1: Tirou 10 = Pontuação 11

Usuário 2: Tirou 5 = Pontuação 16

Usuário 3: Tirou 7 = Pontuação 14

Usuário 4: Tirou 8 = Pontuação 13

2ª rodada:

Usuário 1: Tirou 5 = Pontuação 6

Usuário 2: Tirou 3 = Pontuação 13

Usuário 3: Tirou 4 = Pontuação 10

Usuário 4: Tirou 3 = Pontuação 10

3ª rodada:

Usuário 1: Tirou 9 = Pontuação -3 -> ÚLTIMA RODADA

Usuário 2: Tirou 8 = Pontuação 5

Usuário 3: Tirou 5 = Pontuação 5

Usuário 4: Tirou 10 = Pontuação 0

Final: Vencedor foi Usuário 1
"""
import random

cartas = []
usuarios = [21, 21, 21, 21]
aux = 0
rodada = 1
menor_pontuacao = 21 

for i in range(32):
    cartas.append(random.randint(1, 10))

while (usuarios[0]>0 and usuarios[1]>0 and usuarios[2]>0 and usuarios[3]>0):
    indice = 0
    
    for i in cartas[aux:4*rodada]:
        usuarios[indice] = usuarios[indice] - i
        indice += 1
        
    print(f'{rodada}ª rodada')
    print(f'Usuário 1: Tirou {cartas[aux]} = Pontuação {usuarios[0]}')
    print(f'Usuário 2: Tirou {cartas[aux+1]} = Pontuação {usuarios[1]}')
    print(f'Usuário 3: Tirou {cartas[aux+2]} = Pontuação {usuarios[2]}')
    print(f'Usuário 4: Tirou {cartas[aux+3]} = Pontuação {usuarios[3]}')
    
    rodada += 1
    aux += 4

indice = 0 

while (indice < 4):
    
    if (usuarios[indice] < menor_pontuacao):
        menor_pontuacao = usuarios[indice]
        aux = indice
    indice += 1

print(f'\nFinal: Vencedor foi usuario {aux+1}')