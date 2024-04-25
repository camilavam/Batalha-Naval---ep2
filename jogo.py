#importando bibliotecas
import random 
from funcoes import *
from dados_paises import *

#while play:

#atribuindo o cabeçalho do jogo
titulojogo = "Bem-Vindo a Batalha Naval!!"
tam= len(titulojogo)
titulojogo= '╔'+"═"*tam +'╗'+'\n'+'║'+titulojogo + '║'+"\n"+'╚'+"═"*tam+'╝'
colore("red","\n \n"+ titulojogo + "\n")
