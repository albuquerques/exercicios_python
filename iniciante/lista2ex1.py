#Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" 
#(todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

# Solução

def tri_type(ld1,ld2,ld3):
    lados = [ld1,ld2,ld3]
    lados_unicos = len(set(lados))
    if lados_unicos == 3:
        print('Escaleno')
    elif lados_unicos == 2:
        print('Isósceles')
    elif lados_unicos == 1:
        print('Equilátero')