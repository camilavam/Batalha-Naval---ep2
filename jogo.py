#importa função que gera números aleatórios
from random import randint

#definindo variáveis iniciais
xy = ''
atkXY = ''
comp_valido = ''
jogador_valido = ''
pontuacao_jogador = 5
pontuacao_comp = 5
jogada = 0
posicoes_jogador = []
posicoes_comp = []

#definições do tabuleiro
def tabuleiro(linha,coluna,):
    tab = []
    for i in range(linha):
        tab.append(coluna * [0])
    return tab

def mostrar_tabjogador():
    print("\nTabuleiro do Jogador")
    for c in range(5):
        print(jogador[c])

def mostrar_tabcomp():
    print("\nTabuleiro do computador")
    for d in range(5):
        print(ocultoComputador[d])
    print('----------------------------------')

