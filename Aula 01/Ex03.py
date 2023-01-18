'''
Crie um algoritmo que calcule o IMC (índice de massa corporal).
O IMC é calculado com a formula PESO/(ALTURA ^ 2). 
Para isso, coloque as informações nas variáveis e ao final
apresente o resultado como no exemplo: "O IMC é 18"
'''
peso = float(input("Insira o seu peso em KG: "))
h = float(input("Insira a sua altura em M: "))

imc= peso/(h**2)

print(f'O IMC é {imc:.2f}')