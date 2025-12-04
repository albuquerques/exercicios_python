#Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas. 
#Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.

# Solução

def mediaturma(dicionario):
    notas = dicionario.values()
    soma_notas = sum(notas)
    qtd_alunos = len(dicionario)

    if qtd_alunos == 0: 
        return []

    media = soma_notas / qtd_alunos

    alunos_acimadamedia = []
    for aluno, valor in dicionario.items():
        if valor > media:
            alunos_acimadamedia.append(aluno)

    return alunos_acimadamedia