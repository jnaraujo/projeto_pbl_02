import os
import random
from find import find

import time

def clear():
    os.system("clear")

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
        lista_ordenada.pop(find(s, lista_ordenada)) # remove o valor da lista ordenada

        shuffled_list.append(s) # adiciona o valor na lista aleatoria
    return shuffled_list

def gerar_matriz_aleatoria(n_linhas, n_cols, max_val):
    matriz = gerar_matriz(n_linhas, n_cols)

    valores_aleatorio = gerar_lista_aleatoria(1, max_val+1, n_linhas * n_cols)
    for i in range(n_linhas):
        for j in range(n_cols):
            matriz[i][j] = valores_aleatorio[i * n_cols + j]
    return matriz



def isMatrizCompleta(matriz):
    for row in matriz:
        for col in row:
            if not str(col).isnumeric():
                return False
    return True

'''
    FUNÇÕES DE IMPRIMIR VALORES
'''
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

'''
    FUNÇÕES DE VALIDAÇÕES DE DADOS
'''

def have_the_game_finished(matriz_oculta_tabuleiro1, matriz_oculta_tabuleiro2, rounds, max_rounds, tipo_termino="soma"):
    if tipo_termino == "soma":
        if isMatrizCompleta(matriz_oculta_tabuleiro1) == True or isMatrizCompleta(matriz_oculta_tabuleiro2):
            return True
    else:
        if rounds >= max_rounds or isMatrizCompleta(matriz_oculta_tabuleiro1) == True or isMatrizCompleta(matriz_oculta_tabuleiro2):
            return True
    return False

def pegarMaisProximo(historico, matriz_aleatoria1, matriz_aleatoria2):
    ultimaJogadaJogador1 = historico["jogador1"][-1] # ultima jogada do jogador 1
    ultimaJogadaJogador2 = historico["jogador2"][-1] # ultima jogada do jogador 2

    N_COLS = len(matriz_aleatoria2[0])

    valorSoma1 = []
    valorSoma2 = []

    if ultimaJogadaJogador1["tipo"] == "c":
        valorSoma1 = [matriz_aleatoria1[i][ultimaJogadaJogador1["index"]] for i in range(N_COLS)]
    else:
        valorSoma1 = [matriz_aleatoria1[ultimaJogadaJogador1["index"]][i] for i in range(N_COLS)]
    
    if ultimaJogadaJogador2["tipo"] == "c":
        valorSoma2 = [matriz_aleatoria2[i][ultimaJogadaJogador2["index"]] for i in range(N_COLS)]
    else:
        valorSoma2 = [matriz_aleatoria2[ultimaJogadaJogador2["index"]][i] for i in range(N_COLS)]
    
    valorSoma1 = sum(valorSoma1)
    valorSoma2 = sum(valorSoma2)

    distanciaJogador1 = abs(valorSoma1 - ultimaJogadaJogador1["soma"])
    distanciaJogador2 = abs(valorSoma2 - ultimaJogadaJogador2["soma"])

    if distanciaJogador1 < distanciaJogador2:
        return "jogador1"
    elif distanciaJogador1 > distanciaJogador2:
        return "jogador2"
    else:
        return "empate"

# pegarMaisProximo({
#     "jogador1": [
#         {"tipo": "c", "index": 0, "soma": 1},
#         {"tipo": "c", "index": 1, "soma": 5},
#         {"tipo": "c", "index": 2, "soma": 25},
#     ],
#     "jogador2": [
#         {"tipo": "c", "index": 0, "soma": 4},
#         {"tipo": "c", "index": 1, "soma": 12},
#         {"tipo": "l", "index": 2, "soma": 10},
#     ]}, [
#     [1, 2, 3], # 6
#     [4, 5, 6], # 15
#     [7, 8, 9], # 24
#     #12 15 18
# ], [
#     [1, 2, 3], # 6
#     [4, 5, 6], # 15
#     [7, 8, 9], # 24
#     #12 15 18
# ])


def verificar_somas_matriz(matriz):
    length = len(matriz)
    somasFinais = {
        "linhas": [0]*length,
        "colunas": [0]*length
    }

    somas = {
        "linhas": [0]*length,
        "colunas": [0]*length
    }

    for r in range(length):
        for c in range(length):
            col = matriz[r][c]

            # verifica a linha
            if type(col) != int: # se for um área nao revelada
                somas["linhas"][r] = -999999
                somas["colunas"][c] = -999999
            else:
                somas["linhas"][r] += col
                somas["colunas"][c] += col

    for i in range(length):
        if somas["linhas"][i] > 0:
            somasFinais["linhas"][i] = somas["linhas"][i]
        
        if somas["colunas"][i] > 0:
            somasFinais["colunas"][i] = somas["colunas"][i]
    
    return somasFinais

def eh_valida_entrada_numero_valida(entrada, v_min, v_max):
    if entrada > v_max or entrada < v_min:
        return False
    return True

def receber_e_validar_entrada_numeros(texto_entrada, v_min, v_max):
    continuar = True
    entrada = 0

    while continuar:
        try:
            entrada = int(input(texto_entrada))
            if eh_valida_entrada_numero_valida(entrada, v_min, v_max):
                continuar = False
            else:
                print("Entrada inválida!")
        except ValueError:
            print("Entrada inválida!")
    return entrada # retorna a entrada validada


def eh_valida_entrada_col_row(entrada, n_cols):
    if entrada < 1 or entrada > n_cols:
        return False
    return True 

def receber_e_validar_entrada_col_row(tipo, n_cols, n_rows):
    continuar = True
    entrada = ""

    while continuar:
        try:
            entrada = int(input("Digite o lado da {}: ".format("coluna" if tipo == "c" else "linha")))

            if eh_valida_entrada_col_row(entrada, n_cols):
                continuar = False
            else:
                print("Entrada inválida!")
        except ValueError:
            print("Entrada inválida!")
    return entrada

def eh_valida_entrada_tipo(entrada):
    if entrada not in ["c", "l"]:
        return False
    return True
def receber_e_validar_entrada_tipo():
    continuar = True
    entrada = ""

    while continuar:
        try:
            entrada = input("Onde você deseja somar ( c: coluna ou l: linha ): ")[0].lower()

            if eh_valida_entrada_tipo(entrada):
                continuar = False
            else:
                print("Entrada inválida!")
        except ValueError:
            print("Entrada inválida!")
    return entrada


def dar_pontos(jogador : int, pontos, pontuacao):
    pontuacao["jogador1" if jogador == 0 else "jogador2"] += pontos
    

def analisar_e_dar_pontos(tabuleiro, index, tipo, pontuacao, quemJoga, soma, N_COLS, foiEmpate=False):
    if tipo == "c": # se for coluna
        listaDoLado = [tabuleiro["matriz_aleatoria"][i][index] for i in range(N_COLS)]
        somaLado = tabuleiro["somaLados"]["colunas"][index]
    else: # se for linha
        listaDoLado = [tabuleiro["matriz_aleatoria"][index][i] for i in range(N_COLS)]
        somaLado = tabuleiro["somaLados"]["linhas"][index]

    if somaLado == soma:
        if tipo == "c":
            for i in range(N_COLS):
                tabuleiro["matriz_oculta"][i][index] = listaDoLado[i]
        elif tipo == "l":
            tabuleiro["matriz_oculta"][index] = listaDoLado

        print("Parabéns! Ganhou 3 pontos!")

        dar_pontos(quemJoga, 3, pontuacao)	# adiciona 3 pontos em caso de acertar tudo

    elif somaLado > soma:
        x = y = maxValue = 0

        if tipo == "c":
            maxValue = min(listaDoLado)
            indexValue = listaDoLado.index(maxValue)
            x = indexValue
            y = index
        elif tipo == "l":
            maxValue = min(listaDoLado)
            indexValue = listaDoLado.index(maxValue)
            x = index
            y = indexValue
            
        if tabuleiro["matriz_oculta"][x][y] != "><" and not foiEmpate: # se a posição já estiver preenchida
            print("A soma é maior!")
            print("Como você não abriu uma casa nova, não ganhou ponto.")
        else:
            dar_pontos(quemJoga, 1, pontuacao) # adiciona 1 ponto em caso de mostrar uma casa

            tabuleiro["matriz_oculta"][x][y] = maxValue
            print("A soma é maior!")
            print("Ganhou 1 ponto por mostrar uma casa!")
    else:
        x = y = maxValue = 0
        if tipo == "c":
            maxValue = max(listaDoLado)
            indexValue = listaDoLado.index(maxValue)
            x = indexValue
            y = index
        elif tipo == "l":
            maxValue = max(listaDoLado)
            indexValue = listaDoLado.index(maxValue)
            x = index
            y = indexValue

        if tabuleiro["matriz_oculta"][x][y] != "><" and not foiEmpate: # se a posição já estiver preenchida
            print("A soma é menor!")
            print("Como você não abriu uma casa nova, não ganhou ponto.")
        else:
            dar_pontos(quemJoga, 1, pontuacao) # adiciona 1 ponto em caso de mostrar uma casa
            tabuleiro["matriz_oculta"][x][y] = maxValue
            print("A soma é menor!")
            print("Ganhou 1 ponto por mostrar uma casa!")