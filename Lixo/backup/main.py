from datetime import datetime
import re, json
from pathlib import Path
from bs4 import BeautifulSoup as bs4
from pprint import pprint

"""
_projeto = Path(__file__).parent.absolute()
_dir_fav = Path(_projeto, "Favoritos")
arquivos = list(Path(_dir_fav).glob('*.html'))

def file_to_date(file):
    padrao = r"(.)+(\w+\d+)"
    parte = str(file).split("/")[-1][10:-5]
    if re.match(padrao, parte):
        return datetime.strptime(parte, "%d_%m_%Y").date()
    else:
        return datetime(1, 1, 1)
    

def get_mostRecent_Export(htmls: list):
    #padrao = r"(.)+(\w+\d+)\.html"
    arq_com_data = list(map(lambda k: file_to_date(k), htmls))
    return arq_com_data

    
    '''padronizados = list(filter(lambda fav: fav if re.match(padrao, str(fav)) else "", htmls))
    datas = list(map(lambda data: (datetime.strptime(str(data).split("/")[-1][10:-5], "%d_%m_%Y").date(), data), padronizados))
    datas.sort(key=lambda datas: datas[0])
    return datas'''

pares = get_mostRecent_Export(arquivos)
pprint(pares)
"""

class Downloads():
    def __init__(self):
        self.__file__ = "main.py"
    
    def pst_Downloads(self):
        self._origem = Path(self.__file__).absolute()
        trilha = str(self._origem).split('/')
        return Path(str(f"{trilha[0]}/{trilha[1]}/{trilha[2]}/Downloads"))

    def abrir_pasta(self):
        pasta = self.pst_Downloads()
        if Path.is_dir(pasta):
            return list(Path(pasta).glob('*.html'))
    
    def filtrar_htmls(self):
        arquivos = self.abrir_pasta()
        regex = r'\w{9}_\d{2}_\d{2}_\d{4}'
        filtro = []
        for html in arquivos:
            if re.match(regex, str(html)):
                filtro.append(html)
        return filtro


exports = Downloads()
print(exports.filtrar_htmls())