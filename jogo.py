#importando bibliotecas
import random 
from funcoes import *
from dados_paises import *
import time

#while play:

#atribuindo o cabeçalho do jogo
titulojogo = "Bem-Vindo a Batalha Naval!!"
tam= len(titulojogo)
titulojogo= '╔'+"═"*tam +'╗'+'\n'+'║'+titulojogo + '║'+"\n"+'╚'+"═"*tam+'╝'
colore("red","\n \n"+ titulojogo + "\n")

time.sleep(1)
print("\n\u001b[32mRaposa, se prepare, pois a batalha naval vai começar!!\u001b[0m\n")

#mapa oponente
mapaoponente = cria_mapa(10)

paisoponente, frotaoponente  = random.choice(list(PAISES.items()))

blocosoponente = []
for naviooponente, qntd_naviooponente in frotaoponente.items():
    for tipo_navio, tamanho in CONFIGURACAO.items():
        if naviooponente == tipo_navio:
            num_navios = qntd_naviooponente
            for i in range(num_navios):
                blocosoponente.append(tamanho)

alocacaooponente = aloca_navios(mapaoponente,blocosoponente)

#mapa jogador
mapajogador = cria_mapa(10)

paisjogador = (input("Raposa, digite o nome do país escolhido:"))
primeiraletra = paisjogador[0]
restante = paisjogador[1:]
primeiraletra = primeiraletra.upper()
restante = restante.lower()
paisjogador = primeiraletra + restante

if paisjogador not in PAISES:
    print("Esse país não está disponível")
    paisjogador =(input("Raposa, digite o nome do país escolhido:"))


frotajogador  = PAISES[paisjogador]
print(frotajogador)

linhajogador = (input("Digite a linha do mapa:"))
lista_linha = [1,2,3,4,5,6,7,8,9,10]
if linhajogador not in lista_linha:
    print("Essa linha não está disponível")
    linhajogador =(input("Digite a linha do mapa:"))


colunajogador = (input("Digite a coluna do mapa:"))
lista_coluna = [1,2,3,4,5,6,7,8,9,10]
if colunajogador not in lista_coluna:
    print("Essa coluna não está disponível")
    colunajogador =(input("Digite a coluna do mapa:"))

orientacaojogador = (input("Digite qual a orientação desejada[v,h]:"))
lista_orientacao = ['v','h']
if orientacaojogador not in lista_orientacao:
    print("Essa orientacao não está disponível")
    colunajogador =(input("Digite a orientacão do mapa:"))


blocosjogador = []
for naviojogador, qntd_naviojogador in frotajogador.items():
    for tipo_navio, tamanho in CONFIGURACAO.items():
        if naviojogador == tipo_navio:
            num_navios = qntd_naviojogador
            for i in range(num_navios):
                blocosjogador.append(tamanho)

alocacaojogador = posicao_suporta(mapajogador,blocosjogador,linhajogador,colunajogador,orientacaojogador)

print(alocacaojogador)
