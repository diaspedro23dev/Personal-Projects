from bs4 import BeautifulSoup as bs4
import requests
from ClimaTempo.backend import Backend

class Google:
    def __init__(self) -> None:
        self.conteudoJson = None
        self.urls_nomeadas = str("./_entradas/urls.json")
        self.rotas = str("./_entradas/rotas.json")
        self.urls = []
        self.titulos = {}
        self.partes = ("agora/cidade", "amanha/cidade", "fim-de-semana/cidade", "15-dias/cidade", "cidade")
        self.info = """Definição da classe:
            Procurar pelo json com o local e guardar
            Procurar pelo json com as urls e devolver para a classe
            Se nao existir, crie esse json pela Web"""

    def pegarTitulos(self, links):
        for link in links:
            pagina = self.baixarPagina(link)
            self.titulos[link] = str(f"./_paginas/{pagina.title.text}.html")
        return self.titulos

    def procurarUlrs(self, cortes):
        for corte in cortes:
            corte = corte.split("=")
            try:
                link = corte[1][:-3]
                if link.endswith(self.sufixo) or link.endswith(self.sufixo + "/"):
                    if not (link.find("climatologia") > 0 or link.find("vento") > 0 or link.find("tempoagora") > 0 or link.find("otempo") > 0 or link.find("agroclima") > 0):
                        self.urls.append(link)
            except: continue
        modelo = self.urls[-1].split('/')
        for parte in self.partes:
            url = f"https://www.climatempo.com.br/previsao-do-tempo/{parte}/{modelo[-2]}/{modelo[-1]}"
            if url not in self.urls:
                self.urls.append(url)
        return self.urls
    
    def rasparPagina(self, pagina):
        tags_a = pagina.find_all("a")
        ancoras = list(filter(lambda tag: tag.get('class') == None, tags_a))
        hrefs = list(map(lambda ancora: ancora.get('href'), ancoras))
        return self.procurarUlrs(hrefs)
    
    def baixarPagina(self, url):
        try:
            pagina = requests.get(url)
        except requests.ConnectionError as e:
            return str(f"\nErro de conexão. Nao entrei no Google.\n{e}")
        else:
            return bs4(pagina.text, "html5lib")
    
    def montarLink(self):
        lugar = Backend.abrirJson(self.rotas)
        estado, cidade = lugar.get("estado"), lugar.get("cidade")
        self.sufixo = str(f"{cidade}-{estado}").lower().replace(" ", "")
        url_pre = str("https://www.google.com/search?q=")
        url_meio = str("previsao+climatempo+")
        return str(f"{url_pre}{url_meio}{estado}+{cidade}").replace(" ", "%20").lower()

    def procurarUrls(self):
        urls_json = Backend.abrirJson(self.urls_nomeadas)
        if urls_json:
            return urls_json
        else:
            link = self.montarLink()
            googlePage = self.baixarPagina(link)
            raspas = self.rasparPagina(googlePage)
            return self.pegarTitulos(raspas)

"""
busca = Google()
urls = busca.procurarUrls()
print(urls)
"""

"""
class Raspar_Previsao_Agora:
    def __init__(self):
        self.ct_agora = ""
        self.tempo_hoje = {}

    def abrirPagina(self, newpath):
        caminho = newpath
        try:
            with open(caminho, mode='r', encoding='utf-8') as vsc_html:
                vsc_page = bs4(vsc_html, "html5lib")
        except FileNotFoundError:
            caminho = '.' + caminho
            try:
                with open(caminho, mode='r', encoding='utf-8') as thn_html:
                    thn_page = bs4(thn_html, "html5lib")
            except FileNotFoundError:
                self.ct_agora = str(caminho + " nao existe ainda")
            else:
                self.ct_agora = thn_page
        else:
            self.ct_agora = vsc_page
    
    def get_arcoIris(self):
        try:
            texto = str(self.ct_agora.find("p", attrs={"class": "-gray _flex _align-center"}).text)
        except:
            arcoiris = str("Falha ao capturar esse dado!")
        else:
            fatias = texto.split("\n")
            arcoiris = {fatias[1]: fatias[3]}
            self.tempo_hoje.update(arcoiris)
    
    def get_Titulo(self):
        try:
            titulo = str(self.ct_agora.find("h1", attrs={"class": "-bold -font-18 -dark-blue"}).text).strip("\n ")
        except:
            titulo = str("Falha ao capturar esse dado!")
        else:
            self.tempo_hoje["Título"] = titulo
    
    def get_Icone(self):
        self.tempo_hoje["Icone"] = str(self.ct_agora.find("span", attrs={"class": "col"}).text)
    
    def get_Temp(self):
        self.tempo_hoje["Temperatura"] = str(self.ct_agora.find("span", attrs={"class": "-bold -gray-dark-2 -font-55 _margin-l-20 _center"}).text)
    
    def get_Sens(self):
        div = self.ct_agora.find("div", attrs={"class": "no-gutters -gray _flex _justify-center _margin-t-20 _padding-b-20 _border-b-light-1"})
        self.tempo_hoje["Sensação"] = str(div.find_all("span")[-1].text)
    
    def get_Clown(self):
        div = self.ct_agora.find("div", attrs={"class": "no-gutters -gray _flex _justify-center _margin-t-20 _padding-b-20 _border-b-light-1"})
        self.tempo_hoje["Nuvens"] = str(div.find("span", attrs={"class": "col"}).text)
    
    def get_List(self):
        ul = self.ct_agora.find("ul", attrs={"class": "variables-list _border-b-light-1"})
        divs = list(ul.find_all("div"))
        preText = list(map(lambda div: str(div.text), divs))
        chaveiro = {indice: valor for indice, valor in enumerate(preText)}
        novo_chaveiro = dict()

        for chav, eiro in chaveiro.items():
            if chav%2==0:
                x = eiro
                novo_chaveiro[eiro] = ""
            if chav%2!=0:
                novo_chaveiro[x] = eiro
        
        self.tempo_hoje.update(novo_chaveiro)

    def limparJson(self):
        chaveiro = self.tempo_hoje
        novo_card = {}

        for chav, eiro in chaveiro.items():
            c, e = chav.strip("\n"), eiro.strip("\n")
            novo_card[c] = e
        
        self.tempo_hoje = novo_card
    
    def rasparPagina(self, caminho):
        self.abrirPagina(caminho)
        self.get_arcoIris()
        self.get_Titulo()
        self.get_Icone()
        self.get_Temp()
        self.get_Sens()
        self.get_Clown()
        self.get_List()
        self.limparJson()
        return self.tempo_hoje
"""

#previsao = Raspar_Previsao_Agora()
#hoje = previsao.rasparPagina()
