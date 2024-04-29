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



print(paisoponente)
print(frotaoponente)
print(blocosoponente)
print(alocacaooponente)
