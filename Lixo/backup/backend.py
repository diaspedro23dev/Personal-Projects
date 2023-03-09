import json


#busca = Google()
#urls = busca.procurarUrls()
#print(urls)

class Backend:
    def __init__(self) -> None:
        pass

    def montaCaminhos(self): #ok
        pre = "./_paginas/Previsão do tempo "
        su = " em Campo Largo - PR | Climatempo.html"
        meio = ['para os próximos 15 dias', 'para hoje', 'para amanhã', 'para o fim de semana', 'agora']
        return [str(f"{pre}{cmn}{su}") for cmn in meio]
    
    def abrirJson(self, caminho):
        print("\nTentando abrir o arquivo:", caminho)
        try:
            with open(caminho, mode="r", encoding="utf-8") as arquivo:
                self.conteudo = dict(json.load(arquivo))
        except FileNotFoundError:
            caminho = "." + caminho
            try:
                with open(caminho, mode="r", encoding="utf-8") as arquivo:
                    self.conteudo = dict(json.load(arquivo))
            except FileNotFoundError:
                print(f"Arquivo {caminho} nao existe mesmo. Vou pegar online")
                return None
            else:
                print("Consegui achar pelo Thonny!")
                return self.conteudo
        else:
            print("Consegui achar pelo VScode!")
            return self.conteudo

    def abrirPagina(self, caminho):
        print("\nTentando abrir o arquivo:", caminho)
        try:
            with open(caminho, mode="r", encoding="utf-8") as arquivo:
                self.conteudo = arquivo
        except FileNotFoundError:
            caminho = "." + caminho
            try:
                with open(caminho, mode="r", encoding="utf-8") as arquivo:
                    self.conteudo = arquivo
            except FileNotFoundError:
                print(f"Arquivo {caminho} nao existe mesmo. Vou pegar online")
                return None
            else:
                print("Consegui achar pelo Thonny!")
                return self.conteudo
        else:
            print("Consegui achar pelo VScode!")
            return self.conteudo

    def procurarPaginas(self):
        caminhos = self.montaCaminhos()
        for cmn in caminhos:
            pagina = self.abrirPagina(caminho=cmn)
            if pagina:
                ...
            else:
                print("ver qual nao tem e filtrar para baixar")

b = Backend()
teste = b.procurarPaginas()

#print(teste)



'''
def salvarHTML(links):
    for link, caminho in links.items():
        try:
            existePagina = open(caminho, mode="r", encoding="utf-8")
            print("\nArquivo ja existe:", existePagina.name)
            existePagina.close()
        except FileNotFoundError:
            html = str(busca.baixarPagina(link))
            try:
                with open(caminho, mode="w", encoding="utf-8") as novaPagina:
                    novaPagina.write(html)
                    print("Sucesso ao salvar " + caminho)
            except FileNotFoundError:
                with open("."+caminho, mode="w", encoding="utf-8") as novaPagina:
                    novaPagina.write(html)
                    print("\nSucesso ao salvar " + caminho)
    return links

def criarPaginas():
    y = "Campo Largo - PR"
    pasta = "./_paginas/"
    xs = ("agora", "para hoje", "para amanhã", "para o fim de semana", "para os próximos 15 dias")
    paginas = [str(f"{pasta}Previsão do tempo {page} em {y} | Climatempo.html") for page in xs]
    return paginas

def procurarPaginas():
    paginas = criarPaginas()
    for pagina in paginas:
        try:
            with open(pagina, mode="r", encoding="utf-8") as existePagina:
                print("Achei o arquivo pleo VSCode:", existePagina.name)
        except FileNotFoundError:
            try:
                with open("."+pagina, mode="r", encoding="utf-8") as existePagina:
                    print("Achei o arquivo pelo Thonny:", existePagina.name)
            except FileNotFoundError:
                print("Arquivo não existe mesmo. Procurar online.")
            else:
                pass
        else:
            pass     
'''