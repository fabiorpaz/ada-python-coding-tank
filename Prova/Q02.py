'''
No mercado financeiro, é comum verificar as variações de um ticker ao longo do dia. 
Crie um código que mostre a quantidade de vezes que esse ticker aumentou relativamente o seu valor.
Considere que os últimos valores cotados deste papel estão contidos em uma lista com 24 valores.
'''
import random

variacao = []
quantide_ticker_aumentou = 0 

for i in range(24):
    variacao.append(random.randint(1, 100))
    
ticker = 35

for i in variacao:
    if(i>ticker):
        quantide_ticker_aumentou += 1
    
print(f'Ao longo do dia o ticker aumentou relativamente ao seu valor inicial de {ticker}, {quantide_ticker_aumentou} vezes')