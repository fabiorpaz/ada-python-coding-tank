# Em análise de dados, é comum que a gente use a estatística descritiva para compreensão de uma variável.
# Crie uma função que retorne a média, mediana, 
# valor mínimo e valor máximo de uma lista de valores.
lista = [10, -5, 500, 99, 1]

vmax = max(lista)
vmin = min(lista)
vmean = sum(lista)/len(lista) 

lista.sort()

#Vamos investigar o tamanho da lista
l = len(lista)
if l%2 == 0:
  median = (lista[l//2 - 1] + lista[l//2])/2
else:
  median = lista[l//2]

print(f'Valor máximo = {vmax} \nValor mínimo = {vmin} \nValor médio = {vmean} \nValor mediano = {median}')