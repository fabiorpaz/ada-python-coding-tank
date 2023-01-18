#Escreva um programa que solicite um número inteiro 
#e imprima na tela todos os números de 1 até o número digitado, separado por espaços.
n = int(input('Digite um número: '))
contador = 1
resul = []
while contador<=n:
  resul.append(contador)
  contador +=1

print(resul)