# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def listaMais2(list):
    list.extend(['raio','gelo'])

list = ['agua','terra','fogo','ar']
listaMais2(list)
print(list)