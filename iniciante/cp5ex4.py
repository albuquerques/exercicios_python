# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def funcaoPossivel(nome, list=None):
    if list is None: list = []
    print('Nome: '+nome+' '+str(list))

funcaoPossivel('Ricardo')
funcaoPossivel('Ricardo', [10, 20, 30, 40])