
from Leitor.leitura import ler, hoje
from Gravador.gravacao import gravar
from Informador.informacao import informar

def leitor_climatico(ler, gravar, informar):

    um = ler(hoje)
    dois = gravar(um)
    tres = informar(dois)

    print(tres)

if __name__ == "__main__":

    leitor_climatico(ler, gravar, informar)
