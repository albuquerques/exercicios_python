import numpy as np
import skfuzzy as fuzz

# Universo das variáveis
distancia = np.arange(0, 101, 1)  
curvatura = np.arange(0, 11, 1)    
velocidade = np.arange(0, 11, 1)  

# Funções de pertinência para Distância
dist_perto  = fuzz.trimf(distancia, [0, 0, 30])
dist_media  = fuzz.trimf(distancia, [20, 50, 80])
dist_longe  = fuzz.trimf(distancia, [60, 100, 100])

# Funções de pertinência para Curvatura
curva_reta      = fuzz.trimf(curvatura, [0, 0, 3])
curva_leve      = fuzz.trimf(curvatura, [2, 5, 8])
curva_acentuada = fuzz.trimf(curvatura, [7, 10, 10])

# Funções de pertinência para Velocidade
vel_baixa = fuzz.trimf(velocidade, [0, 0, 4])
vel_media = fuzz.trimf(velocidade, [3, 5, 7])
vel_alta  = fuzz.trimf(velocidade, [6, 10, 10])

# Entradas
distancia_val = 20  
curvatura_val = 9   

# Pertinência da Distância
dist_perto_val = fuzz.interp_membership(distancia, dist_perto, distancia_val)
dist_media_val = fuzz.interp_membership(distancia, dist_media, distancia_val)
dist_longe_val = fuzz.interp_membership(distancia, dist_longe, distancia_val)

# Pertinência da Curvatura
curva_reta_val      = fuzz.interp_membership(curvatura, curva_reta, curvatura_val)
curva_leve_val      = fuzz.interp_membership(curvatura, curva_leve, curvatura_val)
curva_acentuada_val = fuzz.interp_membership(curvatura, curva_acentuada, curvatura_val)

# Regras Fuzzy
# Regra 1
regra1 = np.fmin(dist_perto_val, curva_acentuada_val)
vel_baixa_ativada = np.fmin(regra1, vel_baixa)

# Regra 2
regra2 = np.fmin(dist_longe_val, curva_reta_val)
vel_alta_ativada = np.fmin(regra2, vel_alta)

# Agregação
vel_aggregada = np.fmax(vel_baixa_ativada, vel_alta_ativada)

# Defuzzificação
if np.all(vel_aggregada == 0):
    vel_result = 0
else:
    vel_result = fuzz.defuzz(velocidade, vel_aggregada, 'centroid')

# Classificação do resultado
if vel_result <= 3:
    classificacao = "Baixa"
elif vel_result <= 6:
    classificacao = "Média"
else:
    classificacao = "Alta"

# Saída
print("")
print(f"Grau de pertinência - Distância perto: {dist_perto_val:.2f}")
print(f"Grau de pertinência - Distância média: {dist_media_val:.2f}")
print(f"Grau de pertinência - Distância longe: {dist_longe_val:.2f}")
print("")
print(f"Grau de pertinência - Curva reta: {curva_reta_val:.2f}")
print(f"Grau de pertinência - Curva leve: {curva_leve_val:.2f}")
print(f"Grau de pertinência - Curva acentuada: {curva_acentuada_val:.2f}")
print("")
print(f"Velocidade resultante: {vel_result:.2f} → Classificação: {classificacao}")

#Como funciona esse cálculo do vel_result utilizando "centroid"?
#Por quê ao calcular o grau de pertinência, é considerado o menor valor na hora de ativar o estado de velocidade?
