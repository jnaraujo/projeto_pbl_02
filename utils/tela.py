import os
import time
import random

def clear():
    os.system("clear")

def animacao_inicio():
    rows = 40
    cols = 70
    m = [ [ " " for i in range(cols) ] for j in range(rows) ]

    mostrar_lista_animacao(m)
    for row in range(rows):
        for col in range(cols):
            random_number = random.randint(0, 3)
            if random_number == 3:
                m[row][col] = "|"
        mostrar_lista_animacao(m)    
        time.sleep(0.03)
def mostrar_lista_animacao(matriz):
    clear()
    for row in matriz:
        for col in row:
            print("{}".format(str(col)), end="")
        print()

def mostrar_regras():
    clear()
    print("{:^70s}".format("\033[1;33m---- REGRAS ----\033[0;0m"))
    print("")
    regras = '''
        Objetivo:
        O objetivo do jogo é tentar acerta a soma dos números de uma linha ou coluna.
        Para tal, dois jogadores irão competir para acertar a soma de uma linha ou coluna.

        Como jogar:
        Os jogadores irão colocar quanto eles acham que é a soma da linha ou coluna.
        O jogador que chegar mais próximo da soma ganha um ponto.
        Se ele acertar exatamente, ele ganha 3 pontos.
        Se os dois chegarem próximo da soma, os dois ganham.

        A partida termina quando alguem acertar todas as somas do tabuleiro OU por número de rodadas.


        

    '''
    for linha in regras.split("\n"):
        print(linha)

def mostrar_historico(historico):
    for i in range(len(historico["jogador1"])): # para todas as linhas do historico
        tipo = "coluna" if historico["jogador1"][i]["tipo"] == "c" else "linha" # se for coluna, se nao for, é linha
        print("(Rodada {}) Jogador 1: Tipo: {}; Index: {}; Soma: {}".format(i, tipo, historico["jogador1"][i]["index"], historico["jogador1"][i]["soma"])) # printa o historico do jogador 1
 
        if len(historico["jogador2"]) > i:
            tipo = "coluna" if historico["jogador2"][i]["tipo"] == "c" else "linha"
            print("(Rodada {}) Jogador 2: Tipo: {}; Index: {}; Soma: {}".format(i, tipo, historico["jogador2"][i]["index"], historico["jogador2"][i]["soma"])) # printa o historico do jogador 1
    if "vencedor" in historico and historico["vencedor"] != "empate": # se um dos jogadores ganhou
        print("Resultado da partida: Vitória do jogador {}".format(historico["vencedor"]))
    else:
        print("Resultado da partida: Empate") # se nenhum jogador ganhou

def mostrar_matriz_com_resultados(matriz, show_sum=False, soma={"linhas":[], "colunas": []}):
    index = 0
    for linha in matriz: # para toda linha na matriz
        for i in range(len(linha)): # para toda coluna na linha
            col = linha[i] # pega a coluna
            if i == 0: # se for a primeira coluna
                print(" {:^4s}".format(str(col)), end="")
            else: # se nao for a primeira coluna
                print(" | {:^4s}".format(str(col)), end="")
        
        if show_sum and soma["linhas"][index] > 0: # se for para mostrar a soma e a linha tiver uma soma
            print(" < {:^4s}".format(str(soma["linhas"][index])))
            index += 1
        else:
            print("")
    if show_sum: # se for para mostrar a soma
        print("  \/   " * len(soma["colunas"]))
        for i in range(len(soma["colunas"])):
            if i == 0:
                print(" {:^4s} ".format(str(soma["colunas"][i])), end="")
            else:
                print("  {:^4s} ".format(str(soma["colunas"][i])), end="")
        print("")

def mostrar_matriz(matriz, soma={"linhas":[], "colunas": []}):
    index = 0

    for i in range(len(matriz)): # print o numero da coluna em cima do tabuleiro
        print("    \033[1;33m{:^2s}\033[0;0m ".format(str(i+1)), end="")
    print("")

    for linha in matriz:
        print(" \033[1;33m{:^2s}\033[0;0m".format(str(index+1)), end="") # print o numero da linha ao lado do tabuleiro

        for i in range(len(linha)): # para toda coluna na linha
            col = linha[i] # pega a coluna
            if i == 0: # se for a primeira coluna
                print("\033[1;30m\033[1;47m{:^4s}\033[0;0m".format(str(col)), end="")
            else: # se nao for a primeira coluna
                print(" | \033[1;30m\033[1;47m{:^4s}\033[0;0m".format(str(col)), end="")
        if soma["linhas"][index] > 0: # se a linha tiver uma soma maior que 0
            print(" < \033[1;32m{:^4s}\033[0;0m".format(str(soma["linhas"][index])))
        else: # se nao tiver
            print(" < {:^4s}".format("#"))
        index += 1
    if True:
        print("    \/ " * len(soma["colunas"]))
        print("   ", end="")
        for i in range(len(soma["colunas"])): # para toda coluna na linha
            if soma["colunas"][i] > 0: # se a coluna tiver uma soma maior que 0
                print("\033[1;32m{:^4s}\033[0;0m".format(str(soma["colunas"][i])), end="")
            else: # se nao tiver
                print("{:^4s}".format("#"), end="")
            print("   ", end="")
        print("")    