#Dada uma lista de números, crie uma nova lista usando list comprehension que contenha 
# o quadrado de cada número par da lista original.

# Solução

def dsa_calcula_imc(peso, altura):
    if altura == 0:
        return "Erro: altura não pode ser zero."
    
    imc = peso / (altura ** 2)
    return imc
