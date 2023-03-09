
#import androidhelper

def informar(noticia):
    
    #droid = androidhelper.Android()
    chaves = ("Número do registro: ", "Data de hoje: ", "Previsão: ", "Temperatura Mínima: ", "Temperatura Máxima: ", "Possibilidade de chuva: ", "Volume de chuva: ", "Velocidade do Vento (km/h): ", "Direção do Vento: ", "Umidade Mínima: ", "Umidade Máxima: ", "Nascer do Sol: ", "Por do Sol: ")
    valor = dict(zip(chaves, noticia))

    for a, b in valor.items():
        print(a)
        #droid.ttsSpeak(a)
        print(b)
        #droid.ttsSpeak(b)
    
    return '\n\nfim'


