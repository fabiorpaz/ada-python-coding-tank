# Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.
nums = [5, 10, 50, 100, -20, 0]
pares = 0

for n in range(len(nums)):
  print(f'Índice {n} possui o elemento {nums[n]}')

for num in nums:
  if num%2 == 0:
    pares += 1
print(f'Existem {pares} pares na lista')