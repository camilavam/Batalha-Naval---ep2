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

def imprimir_mapa(mapa, ALFABETO):
    print("   ", end="")
    for letra in ALFABETO:
        print(letra + "  ", end="")
        if letra == "J":
            break
    print('\n', end="")

    for i in range(len(mapa)):
        print(str(i + 1), " ", end="")
        for j in range(len(mapa)):
            if mapa[i][j] == "N":
                print(" "," ", end="")
            else:
                print(mapa[i][j], " ", end="")
        print(str(i + 1))

    print("   ", end="")
    for letra in ALFABETO:
        print(letra + "  ", end="")
        if letra == "J":
            break
    print('\n', end="")


def aloca_navios_player(mapa,blocos):
    for blocos_navio in blocos:
        
            linha = (input('qual a linha a ser alocada? '))
            while linha not in ['1','2','3','4','5','6','7','8','9','10']:
                print("\u001b[33mEssa linha não está disponível\u001b[0m\n")
                linha = int(input('qual a linha a ser alocada? '))
                time.sleep(1)
        
            linha = int(linha)
            coluna = (input('qual a coluna a ser alocada? ')).upper()
            while coluna not in ALFABETO [:10]:
                print("Essa coluna não está disponível")
                coluna = (input('qual a coluna a ser alocada? ')).upper()
                time.sleep(1)
        
            coluna = ALFABETO.find(coluna)
            orientacao = (input('qual a orientação?[h/v] ')).lower()
            for e in orientacao:
                if e == 'h' or e == 'v' or e == 'H' or e == 'V':
                    orientacao = orientacao
                else:
                    print("\nu001b[32mEssa orientação não está disponível\u001b[0m\n")
                    orientacao = int(input('qual a orientação a ser atacada? '))
            linha -= 1
            if posicao_suporta(mapa,blocos_navio,linha,coluna,orientacao):
                
                if orientacao == 'v':
                    for i in range(blocos_navio):
                        mapa[linha + i][coluna] = 'N'
                else:
                    for i in range(blocos_navio):
                        mapa[linha][coluna + i] = 'N'
            mostrar_mapa_jog(mapa,ALFABETO,"situação atual")
                
            
            
    
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
print(aloca_navios)

#Mostra mapa atualizado 
def mostrar_mapa_comp(mapa, ALFABETO,titulo):
    print(titulo)

    print("   ", end="")
    for letra in ALFABETO:
        print(letra + "  ", end="")
        if letra == "J":
            break
    print('\n', end="")

    for i in range(len(mapa)):
        print(str(i + 1), " ", end="")
        for j in range(len(mapa)):
            elemento = mapa[i][j]
            if elemento == 'N':
                print('   ',end="")
            if elemento == 'A':
                print('{0}███{1}'.format(CORES['blue'],CORES['reset']),end="")
            if elemento == 'X':
                print('{0}███{1}'.format(CORES['red'],CORES['reset']),end="")
            if elemento == ' ':
                print(elemento+"  ",end="")
        print(str(i + 1))

    print("   ", end="")
    for letra in ALFABETO:
        print(letra + "  ", end="")
        if letra == "J":
            break
    print('\n', end="")
    return ""

def mostrar_mapa_jog(mapa, ALFABETO,titulo):
    print(titulo)

    print("   ", end="")
    for letra in ALFABETO:
        print(letra + "  ", end="")
        if letra == "J":
            break
    print('\n', end="")

    for i in range(len(mapa)):
        print(str(i + 1), " ", end="")
        for j in range(len(mapa)):
            elemento = mapa[i][j]
            if elemento == 'N':
                print('{0}███{1}'.format(CORES['green'],CORES['reset']),end="")
            if elemento == 'A':
                print('{0}███{1}'.format(CORES['blue'],CORES['reset']),end="")
            if elemento == 'X':
                print('{0}███{1}'.format(CORES['red'],CORES['reset']),end="")
            if elemento == ' ':
                print(elemento+"  ",end="")
        print(str(i + 1))

    print("   ", end="")
    for letra in ALFABETO:
        print(letra + "  ", end="")
        if letra == "J":
            break
    print('\n', end="")
    return ""



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

#função 