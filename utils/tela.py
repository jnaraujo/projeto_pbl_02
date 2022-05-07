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

def mostrar_historico(historico):
    for i in range(len(historico["jogador1"])):
        tipo = "coluna" if historico["jogador1"][i]["tipo"] == "c" else "linha"
        print("(Rodada {}) Jogador 1: Tipo: {}; Index: {}; Soma: {}".format(i, tipo, historico["jogador1"][i]["index"], historico["jogador1"][i]["soma"]))

        if len(historico["jogador2"]) > i:
            tipo = "coluna" if historico["jogador2"][i]["tipo"] == "c" else "linha"
            print("(Rodada {}) Jogador 2: Tipo: {}; Index: {}; Soma: {}".format(i, tipo, historico["jogador2"][i]["index"], historico["jogador2"][i]["soma"]))

    if "vencedor" in historico and historico["vencedor"] != "empate":
        print("Resultado da partida: Vitória do jogador {}".format(historico["vencedor"]))
    else:
        print("Resultado da partida: Empate")

def mostrar_matriz_com_resultados(matriz, show_sum=False, soma={"linhas":[], "colunas": []}):
    index = 0
    for linha in matriz:
        for i in range(len(linha)):
            col = linha[i]
            if i == 0:
                print(" {:^4s}".format(str(col)), end="")
            else:
                print(" | {:^4s}".format(str(col)), end="")
        
        if show_sum and soma["linhas"][index] > 0:
            print(" < {:^4s}".format(str(soma["linhas"][index])))
            index += 1
        else:
            print("")
    if show_sum:
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
        print("\033[1;33m{:^2s}\033[0;0m".format(str(index+1)), end="") # print o numero da linha ao lado do tabuleiro

        for i in range(len(linha)):
            col = linha[i]
            if i == 0:
                print(" \033[1;30m\033[1;47m{:^4s}\033[0;0m".format(str(col)), end="")
            else:
                print(" | \033[1;30m\033[1;47m{:^4s}\033[0;0m".format(str(col)), end="")
        if soma["linhas"][index] > 0:
            print(" < \033[1;32m{:^4s}\033[0;0m".format(str(soma["linhas"][index])))
        else:
            print(" < {:^4s}".format("#"))
        index += 1
    if True:
        print("    \/ " * len(soma["colunas"]))
        print("   ", end="")
        for i in range(len(soma["colunas"])):
            if soma["colunas"][i] > 0:
                print("\033[1;32m{:^4s}\033[0;0m".format(str(soma["colunas"][i])), end="")
            else:
                print("{:^4s}".format("#"), end="")
            print("   ", end="")
        print("")    