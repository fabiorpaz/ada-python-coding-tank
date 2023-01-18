'''
Com o início da automação na entrega de produtos, precisamos ter cuidado para saber 
se a entrega poderá ser realizada ou não. Neste exercício, 
considere que a condição para a entrega do produto ocorre se a caixa 
(com comprimento, largura e profundidade) for capaz de passar pela "portinhola" da casa, 
que possui comprimento e largura. Faça um programa que recebe como entrada as três dimensões da caixa
e as duas dimensões da porta, e retorne Entrega pode ser feita caso seja possível entregar o produto
e Entrega não pode ser feita, caso contrário.
Pense que a caixa pode ser rotacionada para tentar passar pela portinhola
'''
d1 = float(input('Insira a primeira dimensão : '))
d2 = float(input('Insira a segunda dimensão : '))
d3 = float(input('Insira a terceira dimensão : '))

p1 = float(input('Insira a primeira dimensão da portinha: '))
p2 = float(input('Insira a segunda dimensão da portinha: '))

#Vendo as menores dimensões.
if (d1 >= d2) and (d1 >= d3):
  m1 = d2
  m2 = d3
elif (d2 >= d3) and (d2 >= d1):
  m1 = d1 
  m2 = d3
else:
  m1 = d1 
  m2 = d2 

#Se a portinha é retangular 
if ((m1 <= p1) and (m2 <= p2)) or ((m1 <= p2) and (m2 <= p1)):
  print('Entrega pode ser feita')
else:
  print('A entrega não pode ser feita')