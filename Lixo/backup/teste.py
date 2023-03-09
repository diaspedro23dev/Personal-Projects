from pprint import pprint
from bs4 import BeautifulSoup as bs4

previsao_amanha = "./_paginas/Previsão do tempo para amanhã em Curitiba - PR | Climatempo.html"

class Raspar_Previsao_Amanha:
    def __init__(self, clima_amanha):
        self.page_path = clima_amanha
        self.ct_amanha = ""
        self.tempo_amanha = {}

    def abrirPagina(self):
        caminho = self.page_path
        try:
            with open(caminho, mode='r', encoding='utf-8') as vsc_html:
                vsc_page = bs4(vsc_html, "html5lib")
        except FileNotFoundError:
            caminho = '.' + caminho
            try:
                with open(caminho, mode='r', encoding='utf-8') as thn_html:
                    thn_page = bs4(thn_html, "html5lib")
            except FileNotFoundError:
                self.ct_amanha = str(caminho + " nao existe ainda")
            else:
                self.ct_amanha = thn_page
        else:
            self.ct_amanha = vsc_page
    
    def get_arcoIris(self):
        try:
            texto = str(self.ct_amanha.find("p", attrs={"class": "-gray _flex _align-center"}).text)
        except:
            arcoiris = str("Falha ao capturar esse dado!")
        else:
            fatias = texto.split("\n")
            arcoiris = {fatias[1]: fatias[3]}
            self.tempo_amanha.update(arcoiris)
    
    def get_Titulo(self):
        try:
            titulo = str(self.ct_amanha.find("h1", attrs={"class": "-bold -font-18 -dark-blue _margin-r-10 _margin-b-sm-5"}).text).replace("\n", " ").strip()
        except:
            titulo = str("Falha ao capturar esse dado!")
        else:
            self.tempo_amanha["Título"] = titulo
    
    def get_Comparacao(self):
        try:
            par = str(self.ct_amanha.find("p", class_="-gray -line-height-24 _center").text)
            tooltip = str(self.ct_amanha.find("span", class_="tooltip actTriggerGA").get("data-text"))
            conjunto = par + tooltip
        except:
            conjunto = str("Falha ao capturar esse dado!")
        else:
            self.tempo_amanha["Comparacao"] = conjunto
    
    def get_Nuvens(self):
        nuvens = self.ct_amanha.find("div", class_="col-md-6 col-sm-12 _flex _space-between _margin-t-sm-20")
        nuvens_img = nuvens.find_all("img")
        nuvens_p = nuvens.find_all("p")

        try:
            nuvens_img_alt = list(map(lambda alt: alt.get("alt"), nuvens_img))
            nuvens_p_text = list(map(lambda p: p.text, nuvens_p))
            conjunto = dict(zip(nuvens_p_text, nuvens_img_alt))
        except:
            conjunto = str("Falha ao capturar esse dado!")
        else:
            self.tempo_amanha["Nuvens"] = conjunto

    def get_Lista(self):
        ul = self.ct_amanha.find("ul", attrs={"class": "variables-list"})
        helper = {}
        umid, temp = [], []
        rain_k, rain_v = "", ""

        divs = list(ul.find_all("div"))
        spans = list(ul.find_all("span"))
        
        spanText = list(map(lambda span: str(span.text).strip(), spans))
        preText = list(map(lambda div: str(div.text).replace("\n", "").replace(" ", ""), divs))

        for div in preText:
            if div.find("/") > 0:
                helper["Vento"] = div
        for span in spanText:
            if span.find("mm") > 0 and span.find("%") > 0:
                rain_v = span.split("-")
            elif span.startswith("C"):
                rain_k = span
            elif span.find("°") > 0:
                li = int(span[:-1])
                temp.append(li)
            elif span.find("%") > 0 and span.find("mm") < 0:
                li = int(span[:-1])
                umid.append(li)
            elif span.startswith("S"):
                sol_k = span
            elif span.find(":") > 0:
                hora = list(span.split('h'))
                hora.remove('')
                sol_v = {"Nascer": hora[0] + " h", "Por": hora[1] + " h"}
        
        temp.sort()
        umid.sort()

        graus = {"Temperatura": {"min": temp[0], "max": temp[1]}}
        umidade = {"Umidade": {"min": umid[0], "max": umid[1]}}

        helper.update({rain_k: rain_v})
        helper.update(graus)
        helper.update(umidade)
        helper.update({sol_k: sol_v})

        self.tempo_amanha["Lista"] = helper
    
    def get_Mapa(self):
        pass # ate aqui ###########################

    def limparJson(self):
        chaveiro = self.tempo_amanha
        novo_card = {}
        for chav, eiro in chaveiro.items():
            if type(eiro) == str:
                c, e = chav.strip("\n"), eiro.replace("\n", "_").strip()
                novo_card[c] = e
            else:
                novo_card[chav] = eiro
        self.tempo_amanha = novo_card

    def rasparPagina(self):
        self.abrirPagina()
        self.get_Titulo()
        self.get_arcoIris()
        self.get_Comparacao()
        self.get_Nuvens()
        self.get_Lista() # testar essa funcao em outras paginas
        self.get_Mapa()
        self.limparJson()
        
        return self.tempo_amanha 

previsao = Raspar_Previsao_Amanha(previsao_amanha)
amanha = previsao.rasparPagina()

pprint(amanha)


html = ""


def montagem(teste = html):
    return bs4(teste, "html5lib")
montada = montagem(html)

def get_Mapa(mapa):
    mapas = mapa.find("div", attrs={"class": "wrapper-chart"}).get("data-infos")
    return mapas

listagem = get_Mapa(montada)


pprint(listagem)