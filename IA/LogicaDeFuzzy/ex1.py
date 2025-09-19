import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Criando o universo
temp = np.arange(0, 41, 1)
pessoas = np.arange(0, 21, 1)
conforto = np.arange(0, 11, 1)

# Função triângular de temperatura
temp_fria   = fuzz.trimf(temp, [0, 0, 15])
temp_amena  = fuzz.trimf(temp, [10, 20, 30])
temp_quente = fuzz.trimf(temp, [25, 40, 40])

# Função triângular de pessoas
poucas = fuzz.trimf(pessoas, [0, 0, 5]) 
media  = fuzz.trimf(pessoas, [3, 7, 12])  
lotado = fuzz.trimf(pessoas, [8, 15, 20])  

# Função triângular de conforto
conf_baixo = fuzz.trimf(conforto, [0, 0, 4])
conf_medio = fuzz.trimf(conforto, [3, 5, 7])
conf_alto  = fuzz.trimf(conforto, [6, 10, 10])

# Valores de entrada
temp_val = 20
pessoas_val = 10

# Cálculo do grau de pertinência da temperatura
temp_fria_val   = fuzz.interp_membership(temp, temp_fria, temp_val)
temp_amena_val  = fuzz.interp_membership(temp, temp_amena, temp_val)
temp_quente_val = fuzz.interp_membership(temp, temp_quente, temp_val)

# Cálculo do grau de pertinência de pessoas
poucas_val = fuzz.interp_membership(pessoas, poucas, pessoas_val)
media_val  = fuzz.interp_membership(pessoas, media, pessoas_val)
lotado_val = fuzz.interp_membership(pessoas, lotado, pessoas_val)

# Regra 1
regra1 = np.fmin(temp_quente_val, lotado_val)
conf_baixo_ativado = np.fmin(regra1, conf_baixo)

# Regra 2
regra2 = np.fmin(temp_amena_val, media_val)
conf_alto_ativado = np.fmin(regra2, conf_alto)

# Regra 3
regra3 = np.fmin(temp_fria_val, poucas_val)
conf_medio_ativado = np.fmin(regra3, conf_medio)

#Cálculo do conforto aggregado
conforto_aggregado = np.fmax(conf_baixo_ativado,
                             np.fmax(conf_medio_ativado,
                                     conf_alto_ativado))

conforto_result = fuzz.defuzz(conforto, conforto_aggregado, 'centroid')

print("")
print(f"Grau de pertinência da temperatura fria: {temp_fria_val:.2f}")
print(f"Grau de pertinência da temperatura amena: {temp_amena_val:.2f}")
print(f"Grau de pertinência da temperatura quente: {temp_quente_val:.2f}")
print("")
print(f"Grau de pertinência de pessoas poucas: {poucas_val:.2f}")
print(f"Grau de pertinência de pessoas média: {media_val:.2f}")
print(f"Grau de pertinência de pessoas lotado: {lotado_val:.2f}")
print("")

if conforto_result <= 2:
    classificacao = "Péssimo"
elif conforto_result <= 4:
    classificacao = "Ruim"
elif conforto_result <= 6:
    classificacao = "Médio"
elif conforto_result <= 8:
    classificacao = "Bom"
else:
    classificacao = "Excelente"

print(f"Grau de Conforto: {conforto_result:.2f} → Classificação: {classificacao}")
#Como funciona esse cálculo do conforto_result utilizando "centroid"?
#Por quê ao calcular o grau de pertinência, é considerado o menor valor na hora de ativar o estado do conforto?