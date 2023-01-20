'''
Considere agora que você já possui a lista com os palpites dos funcionários da tua empresa
e outra lista com o valor apostado. Crie um código que gere a seguinte tela:
Bolão da Copa do Mundo

Total de votos: n votos

(1) Argentina - x% de votação - Total R$ y
(2) Croácia - x% de votação - Total R$ y
(3) França - x% de votação - Total R$ y
(4) Marrocos - x% de votação - Total R$ y
'''
votos = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 4, 3, 1, 3, 3, 1, 2]
aposta = [10.00, 5.00, 0, 0, 30.00, 3.00, 50.00, 0, 0, 10.00, 5.00, 0, 0, 30.00, 3.00, 50.00, 0, 0]

lista_paises = [0, 0, 0, 0]
total_apostas = [0, 0, 0, 0]

for i in range(len(votos)):
  v = votos[i] -1 
  lista_paises[v] += 1
  total_apostas[v] += aposta[i] 

l = len(votos)
print(f'Bolão da Copa do Mundo! \nTotal de votos: {l}')
print(f'(1) Argentina - {round(100*lista_paises[0]/l,2)}% de votação - Total R$ {round(total_apostas[0],2)}')
print(f'(2) Croácia - {round(100*lista_paises[1]/l,2)}% de votação - Total R$ {round(total_apostas[1],2)}')
print(f'(3) França - {round(100*lista_paises[2]/l,2)}% de votação - Total R$ {round(total_apostas[2],2)}')
print(f'(4) Marrocos - {round(100*lista_paises[3]/l,2)}% de votação - Total R$ {round(total_apostas[3],2)}')