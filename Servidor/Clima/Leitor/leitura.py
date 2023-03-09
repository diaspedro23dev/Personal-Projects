
#import requests as pegador
#from bs4 import BeautifulSoup as filtro
from random import randint as aleatorio
from datetime import datetime, timezone, timedelta

x = datetime.now()
y = timezone(timedelta(hours=-3))
hoje = str(x.astimezone(y).strftime("%d/%m/%Y")) # %H:%M:%S

def ler(hoje):
    #pagina = pegador.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/271/curitiba-pr")
    #sopa = filtro(pagina.text, 'html.parser')

    sql_create = "CREATE TABLE IF NOT EXISTS Clima ("
    sql, insert = "INSERT INTO Clima (", "VALUES ("

    create = {
        "id": "INT NOT NULL UNIQUE",
        "hoje": "TEXT NOT NULL",
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
    dados = {
        "id": aleatorio(1, 999) ** 5,
        "hoje": hoje,
        "previsao": "Hoje será igual a ontem, quente pra caralho! Um Sol pra cada.",
        "temp_min": "34",
        "temp_max": "18",
        "chuva_chance": "0",
        "chuva_prec_mm": "0",
        "vento_vel_kmph": "12",
        "vento_direcao": "NE",
        "umidade_min": "12",
        "umidade_max": "45",
        "nascer_sol": "05h46",
        "por_sol": "19h32",
    }

    for a, b in create.items():
        sql_create += "{} {}, ".format(a, b)
    
    for c, d in dados.items():
        sql += "'{}', ".format(c)
        insert += "'{}', ".format(d)
    
    sql_create = sql_create[:-2] + ");"
    sql, insert = sql[:-2] + ") ", insert[:-2] + ");"
    sql_insert = sql + insert

    query = {
        "banco": "GarotoDoTempo.db",
        "create": sql_create,
        "insert": sql_insert,
        "select": "SELECT * FROM Clima WHERE hoje = '" + hoje + "';"}

    return query
