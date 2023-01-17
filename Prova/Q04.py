'''
Sabemos que uma lista pode conter variáveis de diferentes tipos. 
Crie um programa que divida uma lista lista_baguncada contendo variáveis do tipo int, float e str em três listas distintas, 
cada um contendo um tipo de variável. O programa deve mostrar na tela as três listas geradas.

Exemplo

Entrada: 
lista_baguncada = [5, 0.13, 'Oi', 5.444, 8, 'Ada']

Saída:
lista_int = [5, 8]
lista_float = [0.13, 5.444]
lista_str = ['Oi', 'Ada']
Dica importante!

#Perceba que type(5) retorna a classe do tipo int, e não a string 'int'.

In[0]: type(5)
Out[0] int
'''
lista_baguncada = [5, 0.13, 5.444, 8, 'Ada']

lista_int = [] 
lista_float = [] 
lista_str = []

for i in lista_baguncada: 

    if (type(i) == int): 
        lista_int.append(i) 
    elif(type(i) == float): 
        lista_float.append(i) 
    else: 
        lista_str.append(i)

print('lista_int =', lista_int) 
print('lista_float =', lista_float) 
print('lista_str =', lista_str)