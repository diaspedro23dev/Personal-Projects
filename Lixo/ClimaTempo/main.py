from pathlib import Path

def find_dir_Reserva():
    '''Procurar pela pasta Reserva. Se não existir, crie e retorne o caminho absoluto. Se existir, retorne o caminho absoluto.'''
    main_file = Path(__file__).resolve()
    dir_Reserva = Path(main_file.parent, "Reserva")
    if dir_Reserva.is_dir():
        print("Pasta já existe")
        return dir_Reserva
    else:
        print("Pasta criada")
        dir_Reserva.mkdir(parents=True, exist_ok=True)
        return dir_Reserva


def find_dir_Downloads():
    '''Procurar pela pasta Downloads. Se não existir, retorne vazio. Se existir, retorne o caminho absoluto.'''
    main_file = Path().home()
    dir_Downloads = Path(main_file, "Downloads")
    if dir_Downloads.is_dir():
        return dir_Downloads
    else:
        return None


def from_Downloads_to_Reserva():
    dirR = find_dir_Reserva()
    dirD = find_dir_Downloads()

    if (dirR and dirD):
        print("As 2 pastas existem")
    else:
        print("Deu ruim")
    
    dirD

from_Downloads_to_Reserva()

"""
import re
from datetime import date
from pathlib import Path
from pprint import pprint


class Armario:
    def __init__(self) -> None:
        self.nome = None
        self.pastas = None


class Pasta:
    def __init__(self):
        self.nome = None
        self.caminho = None
        self.arquivos = []


class Arquivo():
    def __init__(self, html):
        self._nome = None
        self._caminho = html
        self._data = None
        self._posicao = False
    
    def set_nome(self):
        self._nome = self._caminho.split('/')[-1]

a = Arquivo('/home/diaspedro/Downloads/favoritos_12_07_2022.html')
a.set_nome()
print(a._nome)
"""