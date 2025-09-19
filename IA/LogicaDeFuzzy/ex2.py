import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Criando o universo
espera = np.arange(0, 61, 1)
satisfação = np.arange(0, 11, 1)
qualidade = np.arange(0, 11, 1)

# Função triângular de espera
espera_curta   = fuzz.trimf(espera, [0, 0, 15])
espera_media  = fuzz.trimf(espera, [10, 25, 40])
espera_longa = fuzz.trimf(espera, [35, 60, 60])

# Função triângular de satisfação
satisfação_baixa = fuzz.trimf(satisfação, [0, 0, 5])
satisfação_media  = fuzz.trimf(satisfação, [3, 5, 8])  
satisfação_alta = fuzz.trimf(satisfação, [7, 10, 10])  

# Função triângular de qualidade
qualidade_ruim = fuzz.trimf(qualidade, [0, 0, 5])
qualidade_aceitavel  = fuzz.trimf(qualidade, [3, 5, 8])  
qualidade_excelente = fuzz.trimf(qualidade, [7, 10, 10])  

# Valores de entrada
espera_val = 10
satisfacao_val = 8

# Cálculo do grau de pertinência de satisfação
satisfação_baixa_val   = fuzz.interp_membership(satisfação, satisfação_baixa, satisfacao_val)
satisfação_media_val  = fuzz.interp_membership(satisfação, satisfação_media, satisfacao_val)
satisfação_alta_val = fuzz.interp_membership(satisfação, satisfação_alta, satisfacao_val)

# Cálculo do grau de pertinência de espera
espera_curta_val = fuzz.interp_membership(espera, espera_curta, espera_val)
espera_media_val  = fuzz.interp_membership(espera, espera_media, espera_val)
espera_longa_val = fuzz.interp_membership(espera, espera_longa, espera_val)

# Regra 1
regra1 = np.fmin(espera_longa_val, satisfação_alta_val)
qualidade_aceitavel_ativado = np.fmin(regra1, qualidade_aceitavel)

# Regra 2
regra2 = np.fmin(espera_curta_val, satisfação_baixa_val)
qualidade_ruim_ativado = np.fmin(regra2, qualidade_ruim)

# Regra 3 (adicional)
regra3 = np.fmin(espera_curta_val, satisfação_alta_val)
qualidade_excelente_ativado = np.fmin(regra3, qualidade_excelente)

# Cálculo da qualidade agreggada
qualidade_aggregada = np.fmax(qualidade_ruim_ativado,
                             np.fmax(qualidade_aceitavel_ativado,
                                     qualidade_excelente_ativado))

# Defuzzificação
if np.all(qualidade_aggregada == 0):
    qualidade_result = 0
else:
    qualidade_result = fuzz.defuzz(qualidade, qualidade_aggregada, 'centroid')

# Classificação
if qualidade_result <= 2:
    classificacao = "Péssima"
elif qualidade_result <= 4:
    classificacao = "Ruim"
elif qualidade_result <= 6:
    classificacao = "Média"
elif qualidade_result <= 8:
    classificacao = "Boa"
else:
    classificacao = "Excelente"

# Saída
print("")
print(f"Grau de pertinência - Satisfação baixa: {satisfação_baixa_val:.2f}")
print(f"Grau de pertinência - Satisfação média: {satisfação_media_val:.2f}")
print(f"Grau de pertinência - Satisfação alta: {satisfação_alta_val:.2f}")
print("")
print(f"Grau de pertinência - Espera curta: {espera_curta_val:.2f}")
print(f"Grau de pertinência - Espera média: {espera_media_val:.2f}")
print(f"Grau de pertinência - Espera longa: {espera_longa_val:.2f}")
print("")
print(f"Qualidade resultante: {qualidade_result:.2f} → Classificação: {classificacao}")

#Como funciona esse cálculo do qualidade_result utilizando "centroid"?
#Por quê ao calcular o grau de pertinência, é considerado o menor valor na hora de ativar o estado de qualidade?