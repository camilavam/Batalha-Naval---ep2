#funções que serão utilizadas no jogo 
from dados_paises import *
import random
import time

def paisoponente_frotaoponente(PAISES):
    return random.choice(list(PAISES.items()))
PAISOPONENTE, FROTAOPONENTE = paisoponente_frotaoponente(PAISES)

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

def aloca_navios_player(mapa,blocos):
    for blocos_navio in blocos:
        while True:
            linha = (input('qual a linha a ser alocada? '))
            if linha not in ['1','2','3','4','5','6','7','8','9','10']:
                print("\nu001b[32mEssa linha não está disponível\u001b[0m\n")
                linha = int(input('qual a linha a ser alocada? '))
                time.sleep(1)
            else:
                linha = int(linha)
                coluna = (input('qual a coluna a ser alocada? '))
                if coluna not in ['1','2','3','4','5','6','7','8','9','10']:
                    print("\nu001b[32mEssa coluna não está disponível\u001b[0m\n")
                    linha = int(input('qual a coluna a ser alocada? '))
                    time.sleep(1)
                else:
                    coluna = int(coluna)
                    orientacao = (input('qual a orientação?[h/v] ')).lower()
                    for e in orientacao:
                        if e == 'h' or e == 'v' or e == 'H' or e == 'V':
                            print('FUNCIONOU PORRA by Camila Mendes!')
                            orientacao = orientacao
                        else:
                            print("\nu001b[32mEssa orientação não está disponível\u001b[0m\n")
                            orientacao = int(input('qual a orientação a ser atacada? '))

            if posicao_suporta(mapa,blocos_navio,linha,coluna,orientacao):
                
                if orientacao == 'v':
                    for i in range(blocos_navio):
                        mapa[linha + i][coluna] = 'N'
                else:
                    for i in range(blocos_navio):
                        mapa[linha][coluna + i] = 'N'

            break
    
    return mapa

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

#Mostra mapa atualizado 
def mostrar_mapa_comp(mapa_comp,ALFABETO): 
    print("COMPUTADOR- {0}".format(PAISOPONENTE)) #Legenda antes de mostrar o mapa do computador

    #Printar letras (parte de cima) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras
        if letra == "J": 
            break 
    print('\n',end="") 

    #Números laterais e linhas do mapa 

    for i in range (len(mapa_comp)): 
        print(str(i+1)," ",end="") 
        for j in range(len(mapa_comp)): 
            print(mapa_comp[i][j], " ", end="") 
        print(str(i+1)) 

    #Printar letras (parte debaixo) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras
        if letra == "J": 
            break 
    print('\n',end="") 
    return "" 


# print(mostrar_mapa_comp(mapa_comp,ALFABETO)) #Nós não vamos printar na tela a posição dos navios do computador, será return. 

###### mostrar_mapa_jog ###### 

def mostrar_mapa_jog(mapa_jogador,ALFABETO): 
    print("JOGADOR-") #Legenda antes de mostrar o mapa do jogador

    #Printar letras (parte de cima) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras
        if letra == "J": 
            break 
    print('\n',end="") 

    #Números laterais e linhas do mapa 

    for i in range (len(mapa_jogador)): 
        print(str(i+1)," ",end="") 
        for j in range(len(mapa_jogador)): 
            print(mapa_jogador[i][j], " ", end="") 
        print(str(i+1)) 

    #Printar letras (parte de cima) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras
        if letra == "J": 
            break 
    print('\n',end="")

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
