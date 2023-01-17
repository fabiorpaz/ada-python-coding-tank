'''
Suponha que você esteja desenvolvendo um sistema para cadastro de adoção de animais.
Crie um código de controle que peça ao usuário o peso do animal, que deve ser um valor real positivo, e a idade, valor inteiro entre 0 e 20. 
O código também deve perguntar ao usuário se o animal já foi vacinado, com respostas possíveis 'Sim' ou 'Não' 
e, caso o animal seja vacinado, o programa deve informar quantos meses se passaram desde a última vacina, que deve ser um valor positivo.
Para cada pergunta feita ao usuário, garanta que o valor fornecido é válido. 
Caso seja um valor inválido, o programa deve indicar uma inconsistência e pedir um novo valor ao usuário, até que seja validado.
'''
peso = float(input('Qual é o peso do animal? '))
while(peso <= 0):
    peso = float(input('Peso invalido, por favor, adicone um peso real e positivo. '))

idade = int(input('Qual é a idade do animal? '))
while(idade<0 or idade>20):
    idade = int(input('Idade invalida, por favor, adicone uma idade entre 0 e 20. '))

vacinado = input('O animal já foi vacinado? ')

while (vacinado != 'Sim' and vacinado != 'Não'):
    vacinado = input('Informação invalida, por favor, adicone apenas Sim ou Não. ')
    
if(vacinado == 'Sim'):
    print('Faz 7 meses desde a sua última vacina') #foi especulada uma data árbitraria já que nao foi solicitado trabalhar com datas.