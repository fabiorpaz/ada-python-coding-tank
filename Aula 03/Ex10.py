'''
Na tua empresa, você está encarregado de mostrar algumas informações sobre o bolão 
de quem deve ser o campeão da Copa do Mundo. 
Para isso, o usuário receberá uma interface com a seguinte informação:
Vote em quem será o campeão da Copa do Mundo!

(1) Argentina
(2) Croácia
(3) França
(4) Marrocos

Caso queira apostar, insira a quantia para o bolão (Use 0 se não quiser apostar)
Desenvolva um código que armazene os votos em uma lista, excluindo os votos que não estejam dentro
das opções disponibilizadas (1 a 4). 
Crie também uma lista que armazene o dinheiro apostado para cada voto válido.
Dica: para simplificar este exercício, crie uma lista vazia em uma célula, 
e em outra célula crie o código para coletar e armazenar o voto em uma lista. 
Futuramente, poderemos utilizar o comando while para fazer este processo de repetição.
'''
bolao = []

palpite = int(input('Insira o teu palpite: ' ))

if palpite in [1,2,3,4]:
  bolao.append(palpite)