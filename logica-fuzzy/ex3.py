import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Universo das variáveis
umidade = np.arange(0, 101, 1)     
temperatura = np.arange(0, 41, 1)   
irrigacao = np.arange(0, 11, 1)    

# Funções de pertinência para Umidade
umidade_seca   = fuzz.trimf(umidade, [0, 0, 40])
umidade_media  = fuzz.trimf(umidade, [30, 50, 70])
umidade_umida  = fuzz.trimf(umidade, [60, 100, 100])

# Funções de pertinência para Temperatura
temp_baixa  = fuzz.trimf(temperatura, [0, 0, 15])
temp_media  = fuzz.trimf(temperatura, [10, 20, 30])
temp_alta   = fuzz.trimf(temperatura, [25, 40, 40])

# Funções de pertinência para Irrigação
irrigacao_pouca    = fuzz.trimf(irrigacao, [0, 0, 4])
irrigacao_moderada = fuzz.trimf(irrigacao, [2, 5, 8])
irrigacao_intensa  = fuzz.trimf(irrigacao, [6, 10, 10])

# Entradas
umidade_val = 20      
temperatura_val = 35 

# Pertinência da Umidade
umidade_seca_val  = fuzz.interp_membership(umidade, umidade_seca, umidade_val)
umidade_media_val = fuzz.interp_membership(umidade, umidade_media, umidade_val)
umidade_umida_val = fuzz.interp_membership(umidade, umidade_umida, umidade_val)

# Pertinência da Temperatura
temp_baixa_val = fuzz.interp_membership(temperatura, temp_baixa, temperatura_val)
temp_media_val = fuzz.interp_membership(temperatura, temp_media, temperatura_val)
temp_alta_val  = fuzz.interp_membership(temperatura, temp_alta, temperatura_val)

# Regra 1: 
regra1 = np.fmin(umidade_seca_val, temp_alta_val)
irrigacao_intensa_ativada = np.fmin(regra1, irrigacao_intensa)

# Agregação
irrigacao_aggregada = irrigacao_intensa_ativada

# Defuzzificação
if np.all(irrigacao_aggregada == 0):
    irrigacao_result = 0
else:
    irrigacao_result = fuzz.defuzz(irrigacao, irrigacao_aggregada, 'centroid')

# Classificação do resultado
if irrigacao_result <= 2:
    classificacao = "Pouca"
elif irrigacao_result <= 6:
    classificacao = "Moderada"
else:
    classificacao = "Intensa"

# Saída
print("")
print(f"Grau de pertinência - Umidade seca: {umidade_seca_val:.2f}")
print(f"Grau de pertinência - Umidade média: {umidade_media_val:.2f}")
print(f"Grau de pertinência - Umidade úmida: {umidade_umida_val:.2f}")
print("")
print(f"Grau de pertinência - Temp baixa: {temp_baixa_val:.2f}")
print(f"Grau de pertinência - Temp média: {temp_media_val:.2f}")
print(f"Grau de pertinência - Temp alta: {temp_alta_val:.2f}")
print("")
print(f"Irrigação resultante: {irrigacao_result:.2f} → Classificação: {classificacao}")

#Como funciona esse cálculo do irrigacao_result utilizando "centroid"?
#Por quê ao calcular o grau de pertinência, é considerado o menor valor na hora de ativar o estado de irrigacao?