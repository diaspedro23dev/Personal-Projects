
import sqlite3 as database

def gravar(query, **kwargs):

    banco = query.get("banco")
    query_create = query.get("create")
    query_insert = query.get("insert")
    query_select = query.get("select")

    conexao = database.connect(banco)
    cursor = conexao.cursor()
    cursor.execute(query_create)
    cursor.execute(query_insert)

    select = cursor.execute(query_select)
    buscado = select.fetchone()
    conexao.commit()
    conexao.close()

    return buscado
