'''
Uma empresa trabalha na confecção de joias e está realizando um teste de controle de qualidade
para verificar se o peso de tal produto está de acordo com o peso especificado, 
que pode ter uma variação aceitável de até 5%. 
Desenvolva um sistema que calcule a proporção de produtos 
que não satisfazem a condição de peso aceitável.
'''
pesos = [5, 10, 10.3, 9.8, 15, 12]
peso_aceitavel = 10
joias_aceitas = 0

for peso in pesos:
  if (peso > 0.95*peso_aceitavel) and (peso < 1.05*peso_aceitavel):
      joias_aceitas += 1

print(f'Apenas {round(100*joias_aceitas/len(pesos),2)}% das joias passaram do teste')