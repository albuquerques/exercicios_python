import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Universo das variáveis
cansaco = np.arange(0, 11, 1)  
sono = np.arange(0, 11, 1)    
acao = np.arange(0, 11, 1)      

# Funções de pertinência para Cansaço
cansaco_baixo = fuzz.trimf(cansaco, [0, 0, 4])
cansaco_medio = fuzz.trimf(cansaco, [3, 5, 7])
cansaco_alto  = fuzz.trimf(cansaco, [6, 10, 10])

# Funções de pertinência para Sono
sono_pouco     = fuzz.trimf(sono, [0, 0, 4])
sono_adequado  = fuzz.trimf(sono, [3, 5, 7])
sono_muito     = fuzz.trimf(sono, [6, 10, 10])

# Funções de pertinência para Ação
acao_alerta       = fuzz.trimf(acao, [0, 0, 4])
acao_descanso     = fuzz.trimf(acao, [3, 5, 7])
acao_forcar_pausa = fuzz.trimf(acao, [6, 10, 10])

# Entradas
cansaco_val = 8  
sono_val = 2     

# Pertinência de Cansaço
cansaco_baixo_val = fuzz.interp_membership(cansaco, cansaco_baixo, cansaco_val)
cansaco_medio_val = fuzz.interp_membership(cansaco, cansaco_medio, cansaco_val)
cansaco_alto_val  = fuzz.interp_membership(cansaco, cansaco_alto, cansaco_val)

# Pertinência de Sono
sono_pouco_val    = fuzz.interp_membership(sono, sono_pouco, sono_val)
sono_adequado_val = fuzz.interp_membership(sono, sono_adequado, sono_val)
sono_muito_val    = fuzz.interp_membership(sono, sono_muito, sono_val)


# Regra 1
regra1 = np.fmin(cansaco_alto_val, sono_pouco_val)
acao_forcar_pausa_ativada = np.fmin(regra1, acao_forcar_pausa)

# Regra 2
regra2 = np.fmin(cansaco_baixo_val, sono_adequado_val)
acao_alerta_ativada = np.fmin(regra2, acao_alerta)

# Agregação
acao_aggregada = np.fmax(acao_forcar_pausa_ativada, acao_alerta_ativada)

# Defuzzificação
if np.all(acao_aggregada == 0):
    acao_result = 0
else:
    acao_result = fuzz.defuzz(acao, acao_aggregada, 'centroid')

# Classificação
if acao_result <= 2:
    classificacao = "Alerta"
elif acao_result <= 6:
    classificacao = "Descanso"
else:
    classificacao = "Forçar pausa"

# Saída
print("")
print(f"Grau de pertinência - Cansaço baixo: {cansaco_baixo_val:.2f}")
print(f"Grau de pertinência - Cansaço médio: {cansaco_medio_val:.2f}")
print(f"Grau de pertinência - Cansaço alto: {cansaco_alto_val:.2f}")
print("")
print(f"Grau de pertinência - Sono pouco: {sono_pouco_val:.2f}")
print(f"Grau de pertinência - Sono adequado: {sono_adequado_val:.2f}")
print(f"Grau de pertinência - Sono muito: {sono_muito_val:.2f}")
print("")
print(f"Ação resultante: {acao_result:.2f} → Classificação: {classificacao}")

#Como funciona esse cálculo do acao_result utilizando "centroid"?
#Por quê ao calcular o grau de pertinência, é considerado o menor valor na hora de ativar o estado de acao?