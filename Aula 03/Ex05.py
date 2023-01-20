#Faça um programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
#Lembrete: Produto escalar entre a (x1, x2) e b (y1, y2) é igual a x1.y1 + x2.y2
a = [5, 10] 
b = [-10, -10]

produto_escalar = 0
if len(a) != len(b):
  print('Os vetores devem ter a mesma dimensão')
else:
  for i in range(len(a)):
    produto_escalar += a[i]*b[i]

print(f'O produto escalar entre {a} e {b} é {produto_escalar}')

