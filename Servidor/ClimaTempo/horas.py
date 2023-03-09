# Horas.py

def batidas_ponto(tempoA, tempoB, tempoC, saldo):
    h_A, m_A = tempoA.split(":")
    h_B, m_B = tempoB.split(":")
    h_C, m_C = tempoC.split(":")
    minutos_A = 60 * int(h_A) + int(m_A)
    minutos_B = 60 * int(h_B) + int(m_B)
    minutos_C = 60 * int(h_C) + int(m_C)
    
    """
tempo = 168
minutos = 0
hora = 0

for x in range(1, tempo+1):
    minutos = minutos + 1
    if minutos == 60:
        hora += 1
        minutos = 0

print(hora, minutos)
"""

batidas_ponto("08:30", "08:30", "08:30", "08:30")