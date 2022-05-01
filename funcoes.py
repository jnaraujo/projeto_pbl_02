import collections
import random


def gerar_matriz(n_linhas, n_cols):
    """
    Função que gera uma matriz de n_linhas x n_cols.
    """
    linha = [0] * n_cols
    matriz = [linha.copy() for x in range(n_linhas)]
    return matriz

def gerar_matriz_oculta(n_linhas, n_cols):
    linha = ["><"] * n_cols
    matriz = [linha.copy() for x in range(n_linhas)]
    return matriz

def somarLadosMatriz(matriz):
    somas_colunas = [0] * len(matriz[0])
    somas_linhas = []
    for linha in matriz:
        for i in range(len(linha)):
            somas_colunas[i] += linha[i]
        somas_linhas.append(sum(linha))
    return {
        "colunas": somas_colunas,
        "linhas": somas_linhas
    }
    


def gerar_lista_aleatoria(v_min, v_max, size):
    lista_ordenada = [i for i in range(v_min, v_max)]
    shuffled_list = []

    for i in range(size):
        s = lista_ordenada[random.randint(0, len(lista_ordenada) - 1)] # retorna um valor aleatorio entre 0 e o tamanho da lista
        lista_ordenada.pop(lista_ordenada.index(s)) # remove o valor da lista ordenada

        shuffled_list.append(s) # adiciona o valor na lista aleatoria
    return shuffled_list

def gerar_matriz_aleatoria(n_linhas, n_cols, max_val):
    matriz = gerar_matriz(n_linhas, n_cols)

    valores_aleatorio = gerar_lista_aleatoria(1, max_val+1, n_linhas * n_cols)
    for i in range(n_linhas):
        for j in range(n_cols):
            matriz[i][j] = valores_aleatorio[i * n_cols + j]
    return matriz


def mostrar_matriz(matriz, show_sum=False, soma={"linhas":[], "colunas": []}):
    index = 0
    for linha in matriz:
        for i in range(len(linha)):
            col = linha[i]
            if i == 0:
                print(" {:^4s}".format(str(col)), end="")
            else:
                print(" | {:^4s}".format(str(col)), end="")
        
        if show_sum and soma["colunas"][index] > 0:
            print(" < {:^4s}".format(str(soma["colunas"][index])))
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

def mostrar_matriz2(matriz, soma={"linhas":[], "colunas": []}):
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
                if i == 0:
                    print(" \033[1;32m{:^4s}\033[0;0m ".format(str(soma["colunas"][i])), end="")
                else:
                    print(" \033[1;32m{:^4s}\033[0;0m ".format(str(soma["colunas"][i])), end="")
            else:
                if i == 0:
                    print("{:^4s}  ".format("#"), end="")
                else:
                    print(" {:^4s}  ".format("#"), end="")
        print("")