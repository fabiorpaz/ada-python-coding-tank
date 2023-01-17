'''
Uma empresa de confecção de vergalhões está automatizando a esteira de produção e gostaria de aumentar o controle de qualidade de seus produtos. 
Para isto, devemos criar um sistema que avalie se o comprimento do vergalhão está dentro do padrão estabelecido pela empresa, que varia entre 1 e 4 metros. 
Produtos que não passam por este teste de qualidade são descartados e considerados reprovados.
Crie uma código que gere duas listas, uma contendo apenas os produtos que passaram pelo teste de qualidade e outra contendo os produtos reprovados. 
No final, mostre na tela:

o percentual de produtos que passaram no teste.
o comprimento mediano dos produtos aprovados.
o comprimento máximo dos produtos reprovados.
a diferença entre o maior e o menor produto.

Considere que existe uma lista prods contendo os comprimentos dos vergalhões, em metros.
'''
produtos_aprovados = []
produtos_falhados = []
prods = []
contar_passaram = 0
comprimento_maximo = 0
i=0
n = int(input('Por favor, informe a quantidade de vergalhões que deseja analisar: '))

while (i<n):
    tam_vergalhao = float(input(f'Por favor, informe qual o tamanho do {i+1} vergalhão em metros: ' ))
    prods.append(tam_vergalhao)
    i += 1

for i in prods:
    if(i>=1 and i<= 4):
        produtos_aprovados.append(i)
        contar_passaram += 1
    else:
        produtos_falhados.append(i)
        if (i > comprimento_maximo):
            comprimento_maximo = i

percentual_passaram = ((100*contar_passaram)/n)

produtos_aprovados.sort()
if (contar_passaram%2 == 0):
    comprimento_mediano1 = produtos_aprovados[contar_passaram//2]
    comprimento_mediano2 = produtos_aprovados[contar_passaram//2 - 1]
    comprimento_mediano = (comprimento_mediano1 + comprimento_mediano2)/2
else:
    comprimento_mediano = produtos_aprovados[contar_passaram//2]

prods.sort()

diferenca_maior_menor = prods[n-1]-prods[0]

print(f' O percentual de produtos que passaram no teste foi {percentual_passaram}%')
print(f' O comprimento mediano dos produtos aprovados foi {comprimento_mediano}')
print(f' O comprimento máximo dos produtos reprovados foi {comprimento_maximo}')
print(f' A diferença entre o maior e o menor produto foi {diferenca_maior_menor}')