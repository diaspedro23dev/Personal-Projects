

print("\n\n")
conversa = {
        "id": "INT NOT NULL UNIQUE",
        "previsao": "TEXT NOT NULL",
        "temp_min": "INT NOT NULL",
        "temp_max": "INT NOT NULL",
        "chuva_chance": "INT NOT NULL",
        "chuva_prec_mm": "INT NOT NULL",
        "vento_vel_kmph": "INT NOT NULL",
        "vento_direcao": "TEXT NOT NULL",
        "umidade_min": "INT NOT NULL",
        "umidade_max": "INT NOT NULL",
        "nascer_sol": "TEXT NOT NULL",
        "por_sol": "TEXT NOT NULL"
    }

def montador(conversa, **kwargs):

    a = "CREATE TABLE IF NOT EXISTS Clima("
    
    for w, z in conversa.items():
        a += "{} {}, ".format(w, z)
    
    k = a[:-2] + ");"

    print (k)

montador(conversa)
print("\n\n")

