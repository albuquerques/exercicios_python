#Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.

# Solução

def multiplicacao_ate10(num):
    for mult in range(1, 11):
        resultado = num * mult
        print(f"{num} * {mult} = {resultado}")
