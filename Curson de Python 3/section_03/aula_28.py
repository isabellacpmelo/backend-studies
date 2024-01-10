"""
CONSTANTE = "Variável" que não pode ser alterada
Muitas condições no mesmo if
   <- Contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 99 #local em que o carro esta na estrada

# Constantes por convêncao em letras maiúsculas
RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local em que o radar 1 esta
RADAR_RANGE = 1 # A distância em que o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')
if carro_passou_radar_1:
    print('Carro passou radar 1')
if carro_multado_radar_1:
    print('Carro foi multado em radar 1')