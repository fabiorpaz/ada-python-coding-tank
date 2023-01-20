#Faça um Programa que peça as 4 notas bimestrais e mostre a média, usando listas.
notas = [] 
for i in range(4):
  nota = float(input(f'Insira a nota {i+1}: '))
  notas.append(nota)

media = sum(notas)/len(notas)
print(f'A média é {media}')