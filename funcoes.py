#funções que serão utilizadas no jogo 

def cria_mapa(N):
    matriz_quadrada = []
    
    for _ in range(N):
        linha = [' '] * N
        matriz_quadrada.append(linha)
   
    return matriz_quadrada