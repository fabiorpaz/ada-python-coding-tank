'''
Em uma estrada municipal, foi desenvolvido um mecanismo para coibir o tráfego de veículos que pesem acima de 20 toneladas (20000 kg). Cada veículo que esteja infringindo esta lei passar por esta rodovia deverá pagar uma multa proporcional ao peso excedente, a uma taxa de R$ 0,50 / kg. Isto é, um carro pesando 21 toneladas deverá pagar um total de R$ 500,00 de multa. Crie um programa que deverá receber uma lista contendo os pesos dos carros que passaram nesta estrada durante um período de tempo e retorne:
a) A quantidade de multas aplicadas.

b) O valor total de multas aplicadas.

c) A proporção de carros que passaram pela estrada e não foram multados.
'''
carros = [50000, 18000, 5000]

multas = []
#Iterando em cada elemento de carros
for carro in carros:
  if carro > 20000:
    valor_multa = 0.5*(carro - 20000) 
    multas.append(valor_multa)

l = len(multas)

if l <= 1:
  print(f'Foi aplicada {l} multa')
else:
  print(f'Foram aplicadas {l} multas')

print(f"Valor total de multas: R${sum(multas)}")
print(f"Proporção de carros não multados: {round(100*(len(carros) - len(multas))/(len(carros)),2)}%")