import random
from utils.find import find

def gerar_matriz(n_linhas, n_cols):
    """
    Função que gera uma matriz de n_linhas x n_cols.
    """
    linha = [0] * n_cols
    matriz = [linha.copy() for x in range(n_linhas)]
    return matriz

def gerar_matriz_oculta(n_linhas, n_cols):
    '''
    Função que gera uma matriz oculta de n_linhas x n_cols.
    '''
    linha = ["><"] * n_cols
    matriz = [linha.copy() for x in range(n_linhas)]
    return matriz

def somarLadosMatriz(matriz):
    '''
    Função que soma os lados de uma matriz.
    '''
    somas_colunas = [0] * len(matriz[0]) # lista de somas das colunas
    somas_linhas = [] # lista de somas das linhas
    for linha in matriz: # para cada linha
        for i in range(len(linha)): # para cada coluna
            somas_colunas[i] += linha[i]  # soma a coluna
        somas_linhas.append(sum(linha)) # adiciona a soma da linha
    return {
        "colunas": somas_colunas,
        "linhas": somas_linhas
    }

def gerar_lista_aleatoria(v_min, v_max, size):
    '''
    Função que gera uma lista aleatória com valores entre v_min e v_max.
    '''
    lista_ordenada = [i for i in range(v_min, v_max)]
    shuffled_list = []

    for i in range(size):
        s = lista_ordenada[random.randint(0, len(lista_ordenada) - 1)] # retorna um valor aleatorio entre 0 e o tamanho da lista
        lista_ordenada.pop(find(s, lista_ordenada)) # remove o valor da lista ordenada

        shuffled_list.append(s) # adiciona o valor na lista aleatoria
    return shuffled_list

def gerar_matriz_aleatoria(n_linhas, n_cols, max_val):
    '''
    Função que gera uma matriz aleatória de n_linhas x n_cols.
    '''
    matriz = gerar_matriz(n_linhas, n_cols) # gera a matriz

    valores_aleatorio = gerar_lista_aleatoria(1, max_val+1, n_linhas * n_cols) # gera uma lista aleatória com número não repetidos
    for i in range(n_linhas): # para cada linha
        for j in range(n_cols): # para cada coluna
            matriz[i][j] = valores_aleatorio[i * n_cols + j] # adiciona o valor na matriz
    return matriz


def isMatrizCompleta(matriz):
    '''
    Função que verifica se uma matriz está completa.
    '''
    for row in matriz:
        for col in row:
            if not str(col).isnumeric(): # se houver um área nao revelada
                return False
    return True

'''
    FUNÇÕES DE VALIDAÇÕES DE DADOS
'''

def have_the_game_finished(matriz_oculta_tabuleiro1, matriz_oculta_tabuleiro2, rounds, max_rounds, tipo_termino="soma"):
    '''
    Função que verifica se o jogo terminou.
    '''
    if tipo_termino == "soma": # se o jogo terminar somente por soma
        if isMatrizCompleta(matriz_oculta_tabuleiro1) == True or isMatrizCompleta(matriz_oculta_tabuleiro2): # se algumas das matrizes estiver completa
            return True
    else: # se o jogo terminar por numero de rodadas OU soma
        if rounds >= max_rounds or isMatrizCompleta(matriz_oculta_tabuleiro1) == True or isMatrizCompleta(matriz_oculta_tabuleiro2): # se estiver completado o número de rodadas OU se algumas das matrizes estiver completa
            return True
    return False

def pegarMaisProximo(historico, matriz_aleatoria1, matriz_aleatoria2):
    '''
        Função que pega as ultimas jogadas do hitórico e verifica qual dos jogadores chegou mais próximo da soma da coluna/linha.
    '''

    ultimaJogadaJogador1 = historico["jogador1"][-1] # ultima jogada do jogador 1
    ultimaJogadaJogador2 = historico["jogador2"][-1] # ultima jogada do jogador 2

    N_COLS = len(matriz_aleatoria2[0])

    valorSoma1 = []
    valorSoma2 = []

    if ultimaJogadaJogador1["tipo"] == "c": # se a ultima jogada do jogador 1 for coluna
        valorSoma1 = [matriz_aleatoria1[i][ultimaJogadaJogador1["index"]] for i in range(N_COLS)] # pega os valores da coluna
    else: # se a ultima jogada do jogador 1 for linha
        valorSoma1 = [matriz_aleatoria1[ultimaJogadaJogador1["index"]][i] for i in range(N_COLS)] # pega os valores da linha
    
    if ultimaJogadaJogador2["tipo"] == "c": # se a ultima jogada do jogador 2 for coluna
        valorSoma2 = [matriz_aleatoria2[i][ultimaJogadaJogador2["index"]] for i in range(N_COLS)] # pega os valores da coluna
    else: # se a ultima jogada do jogador 2 for linha
        valorSoma2 = [matriz_aleatoria2[ultimaJogadaJogador2["index"]][i] for i in range(N_COLS)] # pega os valores da linha
    
    valorSoma1 = sum(valorSoma1) # soma os valores da coluna/linha
    valorSoma2 = sum(valorSoma2) # soma os valores da coluna/linha

    distanciaJogador1 = abs(valorSoma1 - ultimaJogadaJogador1["soma"]) # distancia do jogador 1
    distanciaJogador2 = abs(valorSoma2 - ultimaJogadaJogador2["soma"]) # distancia do jogador 2

    if distanciaJogador1 < distanciaJogador2: # se o jogador 1 estiver mais proximo
        return "jogador1"
    elif distanciaJogador1 > distanciaJogador2: # se o jogador 2 estiver mais proximo
        return "jogador2"
    else: # se os jogadores estiverem na mesma distancia
        return "empate"

def verificar_somas_matriz(matriz):
    '''
        Função que calcula e retorna se os valores já revelados formam somas.
    '''
    length = len(matriz) # pega o tamanho da matriz
    somasFinais = {
        "linhas": [0]*length,
        "colunas": [0]*length
    } # cria um dicionario para as somas finais

    somas = {
        "linhas": [0]*length,
        "colunas": [0]*length
    } # cria um dicionario para as somas

    for r in range(length): # para cada linha
        for c in range(length): # para cada coluna
            col = matriz[r][c] # pega o valor da coluna

            # verifica a linha
            if type(col) != int: # se for um área nao revelada
                somas["linhas"][r] = -999999 # valor muito baixa para invalidar resultado se pelo menos um item não estiver completo
                somas["colunas"][c] = -999999
            else: # se for um valor revelado
                somas["linhas"][r] += col
                somas["colunas"][c] += col

    for i in range(length):
        if somas["linhas"][i] > 0: # se a soma for maior que 0
            somasFinais["linhas"][i] = somas["linhas"][i] # pega a soma
        
        if somas["colunas"][i] > 0: # se a soma for maior que 0
            somasFinais["colunas"][i] = somas["colunas"][i] # pega a soma
    
    return somasFinais

def eh_valida_entrada_numero_valida(entrada, v_min, v_max):
    '''
        Função que verifica se a entrada é um número válido.
    '''
    if entrada > v_max or entrada < v_min: # se a entrada for maior que o valor máximo ou menor que o valor mínimo
        return False
    return True

def receber_e_validar_entrada_numeros(texto_entrada, v_min, v_max):
    '''
        Função que recebe e valida uma entrada de números.

        texto_entrada: texto a ser exibido para o usuário no input
        v_min: valor mínimo
        v_max: valor máximo
    '''
    continuar = True
    entrada = 0

    while continuar: # enquanto a entrada não for válida
        try:
            entrada = int(input(texto_entrada)) # recebe a entrada
            if eh_valida_entrada_numero_valida(entrada, v_min, v_max): # se a entrada for válida
                continuar = False
            else:
                print("Entrada inválida!")
        except ValueError:
            print("Entrada inválida!")
    return entrada # retorna a entrada validada

def eh_valida_entrada_col_row(entrada, n_cols):
    '''
        Função que verifica se a entrada é uma coluna ou linha válida.
    '''
    if entrada < 1 or entrada > n_cols: # se a entrada for maior que o valor máximo ou menor que o valor mínimo
        return False
    return True 

def receber_e_validar_entrada_col_row(tipo, n_cols, n_rows):
    '''
        Função que recebe e valida uma entrada de coluna ou linha.
    '''
    continuar = True
    entrada = ""

    while continuar: # enquanto a entrada não for válida
        try:
            entrada = int(input("Digite o lado da {}: ".format("coluna" if tipo == "c" else "linha"))) # recebe a entrada

            if eh_valida_entrada_col_row(entrada, n_cols): # se a entrada for válida
                continuar = False
            else:
                print("Entrada inválida!")
        except ValueError:
            print("Entrada inválida!")
    return entrada

def eh_valida_entrada_tipo(entrada):
    ''''
        Função que verifica se a entrada é uma coluna ou linha.
    '''
    if entrada not in ["c", "l"]: # se a entrada não for uma coluna (c) ou linha (l)
        return False
    return True

def receber_e_validar_entrada_tipo():
    '''
        Função que recebe e valida uma entrada de tipo.
        Deve ser uma coluna (c) ou linha (l)
    '''
    continuar = True
    entrada = ""

    while continuar:
        try:
            entrada = input("Onde você deseja somar ( c: coluna ou l: linha ): ")[0].lower() # recebe a entrada. pega somente o primeiro caracter e converte para minúsculo

            if eh_valida_entrada_tipo(entrada): # se a entrada for válida
                continuar = False
            else:
                print("Entrada inválida!")
        except ValueError:
            print("Entrada inválida!")
    return entrada

def dar_pontos(jogador : int, pontos, pontuacao):
    '''
        Função que dá pontos ao jogador.
    '''
    pontuacao["jogador1" if jogador == 0 else "jogador2"] += pontos
    
def analisar_matriz(tabuleiro, index, tipo, soma, N_COLS):
    '''
        Função que analisa e dá pontos ao jogador.

        returna o resultado.

        -1: resultado já apreceu
        0: completou a soma
        1: chute maior que o valor correto
        2: chute menor que o valor correto
    '''
    listaDoLado = [] # a lista da linha ou coluna
    somaLado = 0 # soma do lado da linha ou coluna


    if tipo == "c": # se for coluna
        listaDoLado = [tabuleiro["matriz_aleatoria"][i][index] for i in range(N_COLS)] # pega a lista da coluna
        somaLado = tabuleiro["somaLados"]["colunas"][index] # pega a soma da coluna
    else: # se for linha
        listaDoLado = [tabuleiro["matriz_aleatoria"][index][i] for i in range(N_COLS)] # pega a lista da linha
        somaLado = tabuleiro["somaLados"]["linhas"][index] # pega a soma da linha

    if somaLado == soma: # se o jogador acertou a soma da linha ou coluna
        jaFoiRevelada = False # se a soma já foi revelada

        if tipo == "c":
            qnt_reveladas = 0
            for i in range(N_COLS):
                if tabuleiro["matriz_oculta"][i][index] != "><":
                    qnt_reveladas += 1
                
            if qnt_reveladas == N_COLS:
                jaFoiRevelada = True
            
            if not jaFoiRevelada:
                for i in range(N_COLS):
                    tabuleiro["matriz_oculta"][i][index] = listaDoLado[i] # coloca os números na coluna da matriz oculta
        elif tipo == "l":
            qnt_reveladas = 0
            for i in range(N_COLS):
                if tabuleiro["matriz_oculta"][index][i] != "><":
                    qnt_reveladas += 1
            
            if qnt_reveladas == N_COLS:
                jaFoiRevelada = True
            if not jaFoiRevelada:
                tabuleiro["matriz_oculta"][index] = listaDoLado # coloca os números na linha matriz oculta

        if not jaFoiRevelada:
            return 0 # retorna 0 para indicar que o jogador acertou a soma
        else:
            return -1 # retorna -1 para indicar que a casa já tinha sido aberta

    elif somaLado > soma: # se a soma do jogador for maior que a soma da coluna ou linha
        x = y = minValue = 0

        if tipo == "c":
            minValue = min(listaDoLado) # pega o menor número da coluna
            indexValue = listaDoLado.index(minValue) # pega o indice do minValor
            x = indexValue
            y = index
        elif tipo == "l":
            minValue = min(listaDoLado) # pega o menor número da coluna
            indexValue = listaDoLado.index(minValue) # pega o indice do minValor
            x = index
            y = indexValue
            
        if tabuleiro["matriz_oculta"][x][y] != "><": # se a posição já estiver preenchida
            return -1 # retorna -1 para indicar que a casa já tinha sido aberta
        else:
            # dar_pontos(quemJoga, 1, pontuacao) # adiciona 1 ponto em caso de mostrar uma casa
            tabuleiro["matriz_oculta"][x][y] = minValue
        
        return 1 # retorna 1 para indicar que o chute foi maior que a soma da coluna ou linha
    else:
        x = y = maxValue = 0
        if tipo == "c":
            maxValue = max(listaDoLado) # pega o maior número da coluna
            indexValue = listaDoLado.index(maxValue) # pega o indice do maxValor
            x = indexValue
            y = index
        elif tipo == "l":
            maxValue = max(listaDoLado) # pega o maior número da coluna
            indexValue = listaDoLado.index(maxValue) # pega o indice do maxValor
            x = index
            y = indexValue

        if tabuleiro["matriz_oculta"][x][y] != "><": # se a posição já estiver preenchida
            return -1 # retorna -1 para indicar que a casa já tinha sido aberta
        else:
            # dar_pontos(quemJoga, 1, pontuacao) # adiciona 1 ponto em caso de mostrar uma casa
            tabuleiro["matriz_oculta"][x][y] = maxValue
        return 2 # retorna 2 para indicar que o chute foi menor que a soma da coluna ou linha