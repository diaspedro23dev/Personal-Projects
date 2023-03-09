from pathlib import Path
import json


class Servidor:
    def __init__(self, lugar) -> None:
        self.rascunho = lugar
        self.consts = ('Da', 'Das', 'De', 'Des', 'Do', 'Dos')
        self.estados_json = "./_bussola/estados.json"
        self.tipos = ["agora", "hoje", "amanhã", "o fim de semana", "os próximos 15 dias"]
 
    def arruma_cidade(self, cidade: str):
        fatias = cidade.split(' ')
        nova_cidade = ""
        for fatia in fatias:
            if fatia in self.consts:
                fatia = fatia.lower()
            nova_cidade += fatia + " "
        return nova_cidade.strip()
    
    def arruma_estado(self, estado: str):
        estado = estado.replace(" ", "")
        if len(estado) == 2:
            return estado.upper()
        else:
            with open(self.estados_json, mode="r", encoding="utf-8") as json_estados:
                return json.load(json_estados)[estado].upper()
    
    def forma_sufixo(self, pre: str, fixo: str):
        pre = pre.replace(" ", "")
        return str(f"{pre}-{fixo}").lower()
    
    def html_path(self, cid: str, est: str):
        return [str(f"Previsão do tempo para {cid} - {est} em {tipo} | Climatempo.html") for tipo in self.tipos]
    
    def localizacao(self):
        cid, est = self.rascunho.split('/')
        cidade = self.arruma_cidade(cid.title())
        estado = self.arruma_estado(est)
        chaves = {
            "lugar": {"estado": estado, "cidade": cidade, "sufixo": self.forma_sufixo(cidade, estado)}, 
            "paths": self.html_path(cidade, estado)}
        return chaves

    def montar_diagrama(self):
        localizacao = self.localizacao()
        pathsIN = localizacao["paths"]
        pathsOUT = {}
        for path_html in pathsIN:
            if Path(path_html).is_file():
                print("arquivo existe")
                pathsOUT[path_html] = True
            else:
                print("html nao existe")
                pathsOUT[path_html] = False
        localizacao.update({"paths": pathsOUT})
        return localizacao