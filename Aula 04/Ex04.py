#Faça um programa em que o usuário digite números quaisquer que encerrará 
#no momento em que o valor 0 seja digitado. Ao final diga qual foi o maior número digitado.
maior = 0
n = 1
while(n != 0):
  if n > maior: 
    n = maior 
  n = int(input("Insira um número: "))
print("O maior número é {}".format(maior))
