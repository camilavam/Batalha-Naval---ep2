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
        print(computadorOculto[d])
    print('----------------------------------')

jogador = tabuleiro(5,10)
computador = tabuleiro(5,10)
computadorOculto = tabuleiro(5,10)

#pede a posição ao jogador
for i in range(5):
    while jogador_valido != 'válido':
        xy = str(input(f'Digite a posição do {i} do barco, para x de 0 à 4, para y de 0 à 9(x,y): '))
        if xy not in posicoes_jogador:
            jogador[int(xy[0])][int(xy[1])] = 1
            posicoes_jogador.append(xy)
            jogador_valido = 'válido'

    while comp_valido != 'válido':
        xy = str(randint(0,4)) + str(randint(0,9))
        if xy not in posicoes_comp:
            computador[int(xy[0])][int(xy[1])] = 1
            posicoes_comp.append(xy)
            comp_valido = 'válido'
    jogador_valido = ''
    comp_valido = ''

mostrar_tabcomp()
mostrar_tabjogador()



