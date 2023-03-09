import requests
from bs4 import BeautifulSoup

class Web:
    def __init__(self, chaves) -> None:
        self.conjunto = chaves
    
    def montarLink(self, kit: dict):
        partes = kit["lugar"].values()
        cid, est, suf = partes
        return cid, est, suf
    
    def fazer_alguma_coisa(self):
        teste = self.montarLink(self.conjunto)
        return teste
