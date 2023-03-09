""" Calculo de horas trabalhadas.
A partir das 3 batidas, eu mostro o horário da última batida """

def horas_trabalhadas(pontoA , pontoB , pontoC):
    tempo_total = 8 * 60
    almoco = 1 * 60
        
    x1 = pontoA.split('h')
    x2 = pontoB.split('h')
    x3 = pontoC.split('h')

    y1 = x1[1].split('m')
    y2 = x2[1].split('m')
    y3 = x3[1].split('m')

    x1, x2, x3 = int(x1[0]), int(x2[0]), int(x3[0])
    y1, y2, y3 = int(y1[0]), int(y2[0]), int(y3[0])

    horas_antes = int(x2 - x1) * 60
    minutos_antes = int(y2 - y1)
    antes_almoco = int(horas_antes + minutos_antes)
    depois_almoco = int(tempo_total - antes_almoco)
    
    hora_final = depois_almoco // 60
    min_final = depois_almoco - (hora_final * 60)
    
    hora, minuto = hora_final + x3, min_final + y3
    
    if (hora < 10) or (minuto < 10):
        pontoD = str(f"0{hora}h 0{minuto}m")
    else:
        pontoD = str(f"{hora}h {minuto}m")
    
    print("Hora final:", pontoD)

    sobra = almoco - ((x3 - x2) * 60) + (y3 - y2)
    print(f"Sobra do almoco: {sobra}min")



horas_trabalhadas("09h59m", "12h41m", "14h51m")