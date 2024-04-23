#funções que serão utilizadas no jogo 

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