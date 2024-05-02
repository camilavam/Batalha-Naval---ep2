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

#mostra paises e frotas
for k, pais in enumerate(PAISES):
    print (f'{k + 1}:', pais)
    for n, item in enumerate(PAISES[pais]):
        print('     ', f'{n + 1}:', item)
    print("="*20)
#mapa oponente
mapaoponente = cria_mapa(10)

# paisoponente, frotaoponente  = random.choice(list(PAISES.items()))
blocosoponente = []
for naviooponente, qntd_naviooponente in FROTAOPONENTE.items():
    for tipo_navio, tamanho in CONFIGURACAO.items():
        if naviooponente == tipo_navio:
            num_navios = qntd_naviooponente
            for i in range(num_navios):
                blocosoponente.append(tamanho)

alocacaooponente = aloca_navios(mapaoponente,blocosoponente)
time.sleep(1)
print('\n\u001b[32mLocalizando o país inimigo...\u001b[0m\n')
time.sleep(1)
print(f'\n\u001b[32mSeu oponente será:\u001b[0m\n')
time.sleep(1)
print(PAISOPONENTE)
time.sleep(1)
print(f'\n\u001b[32mA batalha não será fácil...Raposa, chegou a hora de ser calculista, analise as frotas para tomar uma grande decisão... \u001b[0m\n')


#mapa jogador
mapajogador = cria_mapa(10)
paisjogador = (input("Raposa, digite o nome do país escolhido:")).capitalize()
# primeiraletra = paisjogador[0]
# restante = paisjogador[1:]
# primeiraletra = primeiraletra.upper()
# restante = restante.lower()
# paisjogador = primeiraletra + restante

if paisjogador not in PAISES:
    print("\n\u001b[32mEsse país não está disponível\u001b[0m\n")
    paisjogador =(input("Raposa, digite o nome do país escolhido:\u001b[0m\n")).capitalize()


frotajogador  = PAISES[paisjogador]
print('\n\u001b[32mÓtima escolha raposa! A sua frota será:\u001b[0m\n')

# def mapa_comp(mapajogador, ALFABETO)
# print(mapa_comp)
# mapa_comp = mostrar_mapa_comp(mapaoponente, ALFABETO)
# print(mapa_comp)
print(frotajogador)
print('O computador posicionou suas tropas')
# print("COMPUTADOR- {0}".format(PAISOPONENTE))
# espaçamento_inicial = "   "
# letras = [letra + "  " for letra in ALFABETO[:ALFABETO.index('J')+1]]
# print(espaçamento_inicial + ''.join(letras))


time.sleep(1)

blocosjogador = []
for naviojogador, qntd_naviojogador in frotajogador.items():
    for tipo_navio, tamanho in CONFIGURACAO.items():
        if naviojogador == tipo_navio:
            num_navios = qntd_naviojogador
            for i in range(num_navios):
                blocosjogador.append(tamanho)

alocacaojogador = aloca_navios_player(mapajogador,blocosjogador)

print(alocacaojogador)

quem_joga = random.randint(0, 1)

while not foi_derrotado(mapajogador) and not foi_derrotado(mapaoponente):
    if quem_joga == 0:
        print('Computador está atacando')
        time.sleep(1)

        # sortear linha e coluna de ataque
        linha_ataque_comp = random.randint(0,len(mapajogador)-1)
        coluna_ataque_comp = random.randint(0,len(mapajogador)-1)
        while mapajogador[linha_ataque_comp][coluna_ataque_comp] == 'X' or mapajogador[linha_ataque_comp][coluna_ataque_comp] == 'A':
            linha_ataque_comp = random.randint(0,len(mapajogador)-1)
            coluna_ataque_comp = random.randint(0,len(mapajogador)-1)
        if mapajogador[linha_ataque_comp][coluna_ataque_comp] == 'N':
            mapajogador[linha_ataque_comp][coluna_ataque_comp] = 'X'
            if foi_derrotado(mapajogador) == True:
                print('Não foi dessa vez =(, você perdeu!')
            else:
                print(f'Jogador: \n {mapajogador}')
                print(f'Oponente: \n {mapaoponente}')
                quem_joga = 1
        else:
            mapajogador[linha_ataque_comp][coluna_ataque_comp] = 'A'
            print(f'Jogador: \n {mapajogador}')
            print(f'Oponente: \n {mapaoponente}')
            quem_joga = 1
    else:
        print('está na hora de atacar')
        time.sleep(1)
        linha_ataque = int(input('qual linha você irá atacar? '))
        coluna_ataque = int(input('qual coluna você irá atacar? '))
        while mapaoponente[linha_ataque][coluna_ataque] == 'X' or mapaoponente[linha_ataque][coluna_ataque] == 'A':
            linha_ataque = int(input('qual linha você irá atacar? '))
            coluna_ataque = int(input('qual coluna você irá atacar? '))
        if mapaoponente[linha_ataque][coluna_ataque] == 'N':
            mapaoponente[linha_ataque][coluna_ataque] = 'X'
            if foi_derrotado(mapaoponente) == True:
                print('Parabéns, você ganhou!!')
            else:
                print(f'Jogador: \n {mapajogador}')
                print(f'Oponente: \n {mapaoponente}')
                quem_joga = 1
        else:
            mapaoponente[linha_ataque][coluna_ataque] = 'A'
            print(f'Jogador: \n {mapajogador}')
            print(f'Oponente: \n {mapaoponente}')
            quem_joga = 1