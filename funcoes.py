#funções que serão utilizadas no jogo 
from dados_paises import *

#função que irá criar o mapa da batalha naval
def cria_mapa(N):
    matriz_quadrada = []
    
    for _ in range(N):
        linha = [' '] * N
        matriz_quadrada.append(linha)
   
    return matriz_quadrada

#função que irá verificar se a posição dita cabe na matriz e se ela já foi alocada ou não
def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    mapa_tam = len(mapa)
    
    if linha < 0 or coluna < 0 or linha >= mapa_tam or coluna >= mapa_tam:
        return False
    
    if orientacao != 'v' and orientacao != 'h':
        return False
    
    if orientacao == 'v':
        if linha + blocos > mapa_tam:
            return False
    else:
        if coluna + blocos > mapa_tam:
            return False
    
    for i in range(blocos):
        if orientacao == 'v':
            if mapa[linha + i][coluna] != ' ':
                return False
        else:
            if mapa[linha][coluna + i] != ' ':
                return False
    
    return True


#função que aloca os navios no tabuleiro para o computador de forma automática - utilizando como base a função posicao_suporta feita acima
import random as random

def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    mapa_tam = len(mapa)
    
    if linha < 0 or coluna < 0 or linha >= mapa_tam or coluna >= mapa_tam:
        return False
    
    if orientacao != 'v' and orientacao != 'h':
        return False
    
    if orientacao == 'v':
        if linha + blocos > mapa_tam:
            return False
    else:
        if coluna + blocos > mapa_tam:
            return False
    
    for i in range(blocos):
        if orientacao == 'v':
            if mapa[linha + i][coluna] != ' ':
                return False
        else:
            if mapa[linha][coluna + i] != ' ':
                return False
    
    return True

def aloca_navios(mapa, blocos):
    mapa_tam = len(mapa)
    
    for blocos_navio in blocos:
        while True:
            linha = random.randint(0, mapa_tam - 1)
            coluna = random.randint(0, mapa_tam - 1)
            orientacao = random.choice(['h', 'v'])

            if posicao_suporta(mapa, blocos_navio, linha, coluna, orientacao):
               
                if orientacao == 'v':
                    for i in range(blocos_navio):
                        mapa[linha + i][coluna] = 'N'
                else:
                    for i in range(blocos_navio):
                        mapa[linha][coluna + i] = 'N'
                break
    
    return mapa

#função que verifica se ainda há algum navio na matriz
def foi_derrotado(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True

#função que vai colorir 
def colore(cor, texto):
    txt = CORES[cor] + texto + CORES["reset"]
    print(txt)
    return
