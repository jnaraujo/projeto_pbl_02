""" /*******************************************************************************

    Autor: Jônatas Araújo Silva Santos
    Componente Curricular: Algoritmos I
    Concluido em: 06/04/2022
    Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
    trecho de código de outro colega ou de outro autor, tais como provindos de livros e
    apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código de
    outra autoria que não a minha está destacado com uma citação para o autor e a fonte do
    código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

******************************************************************************************/ """

########## LIBS ##########

import funcoes
import os


########## CONSTANTES ##########

########## Variáveis ##########

N_COLS = 1 # Número de colunas do tabuleiro
N_LINHAS = 1 # Número de linhas do tabuleiro
QNT_RAND_NUNS = 1 # Quantidade de números aleatórios

historico_jogadas = {
    "jogador1": [],
    "jogador2": [],
    "vencedor": "",
}
pontuacao = {
    "jogador1": 0,
    "jogador2": 0,
}

max_rounds = 0

tipo_termino = "soma" # como o jogador desejar terminar o jogo; "soma" ou "round"


def main():

    # funcoes.animacao_inicio()

    funcoes.clear()

    print("="*70)
    print('''
    /$$$$$            /$$$$$$            /$$$$$$$$                    
   |__  $$           /$$__  $$          | $$_____/                    
      | $$  /$$$$$$ | $$  \__/  /$$$$$$ | $$        /$$$$$$$  /$$$$$$ 
      | $$ /$$__  $$|  $$$$$$  /$$__  $$| $$$$$    /$$_____/ /$$__  $$
 /$$  | $$| $$  \ $$ \____  $$| $$  \ $$| $$__/   |  $$$$$$ | $$  \ $$
| $$  | $$| $$  | $$ /$$  \ $$| $$  | $$| $$       \____  $$| $$  | $$
|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$$$$$$$ /$$$$$$$/|  $$$$$$$
 \______/  \______/  \______/  \______/ |________/|_______/  \____  $$
                                                                  | $$
                                                                  | $$
                                                                  |__/
    ''', end="\n")
    print("{:^70s}".format("Bem vindo ao:"))
    print("{:^70s}".format("Jogo das Somas Esquecidas"))
    print("="*70)

    print()

    print("{:^70s}".format("Modos de jogo:\n"))

    print("Quantos tabuleiros?")
    print("[0] {:<8} [1] {:<8}".format("Um tabuleiro", "Dois tabuleiros"))
    modo = funcoes.receber_e_validar_entrada_numeros("", 0, 1) # Recebe e valida o modo de jogo

    print("Qual o nível?")
    print("[0] {:<8} [1] {:<8} [2] {:<8}".format("Fácil", "Médio", "Difícil"))
    nivel = funcoes.receber_e_validar_entrada_numeros("", 0, 2) # Recebe e valida a entrada do nível


    print("Como você deseja terminar a partida?")
    print("[0] Quando alguem completar o tabuleiro")
    print("[1] Por número de rounds")
    termino = funcoes.receber_e_validar_entrada_numeros("", 0, 1) # Recebe e valida a entrada do termino

    if termino == 0: # Se o termino for por completar o tabuleiro
        tipo_termino = "soma"
        max_rounds = 99999
    elif termino == 1: # Se o termino for por número de rounds
        tipo_termino = "round"
        max_rounds = funcoes.receber_e_validar_entrada_numeros("Quantas rodadas? (min: 1 e max: 99) ", 1, 99) # Recebe e valida a entrada do número de rounds
        while max_rounds % 2 == 0:
            print("O número de rounds deve ser impar")
            max_rounds = funcoes.receber_e_validar_entrada_numeros("Quantas rodadas? (min: 1 e max: 99) ", 1, 99)

    if nivel == 0: # facil
        N_COLS = 3
        N_LINHAS = 3
        QNT_RAND_NUNS = 30
    elif nivel == 1: # medio
        N_COLS = 4
        N_LINHAS = 4
        QNT_RAND_NUNS = 60
    elif nivel == 2: # dificil
        N_COLS = 5
        N_LINHAS = 5
        QNT_RAND_NUNS = 100

    ''''
        Gerando tabuleiros
    '''

    # TABULEIRO 1
    tabuleiro1 = {
        "matriz_aleatoria": funcoes.gerar_matriz_aleatoria(N_LINHAS, N_COLS, QNT_RAND_NUNS), # matriz aleatoria gerada pelo sistema
        "matriz_oculta": funcoes.gerar_matriz_oculta(N_LINHAS, N_COLS), # matriz inicialmente oculta que é mostrada na tela; é modificada com o tempo
        "somaLados": [], # quando vale a soma das colunas e linhas
    }
    tabuleiro1["somaLados"] = funcoes.somarLadosMatriz(tabuleiro1["matriz_aleatoria"])

    # TABULEIRO 2
    tabuleiro2 = {
        "matriz_aleatoria": funcoes.gerar_matriz_aleatoria(N_LINHAS, N_COLS, QNT_RAND_NUNS),
        "matriz_oculta": funcoes.gerar_matriz_oculta(N_LINHAS, N_COLS),
        "somaLados": [],
    }
    tabuleiro2["somaLados"] = funcoes.somarLadosMatriz(tabuleiro2["matriz_aleatoria"])

    #################################


    print(tabuleiro1)

    input()

    # VARIÁVEIS DE JOGO
    quemJoga = 0 # 0 = jogador1, 1 = jogador2
    rodada = 0 # contador de rodadas

    while not funcoes.have_the_game_finished(tabuleiro1["matriz_oculta"], tabuleiro2["matriz_oculta"], rodada, max_rounds, tipo_termino): # enquanto não tiver todas as posições preenchidas
        funcoes.clear()
        
        tabuleiro = {}

        if quemJoga == 0: # quando for o jogador 1 de novo
            rodada += 1 # adiciona 1 as rodadas

        if modo == 1: # modo de 2 tabuleiros
            if quemJoga == 0:
                tabuleiro = tabuleiro1
            else:
                tabuleiro = tabuleiro2
        else:
            tabuleiro = tabuleiro1

        print()

        print("="*70)
        print("{:^70s}".format("Rodada {:.0f}".format(rodada-1)))
        print("{:^70s}".format("Quem joga: " + ("Jogador 1" if quemJoga == 0 else "Jogador 2")))
        print("{:^70s}".format("Jogador 1 | {} x {} | Jogador 2".format(pontuacao["jogador1"], pontuacao["jogador2"])))
        print("="*70)

        funcoes.mostrar_matriz_com_resultados(tabuleiro["matriz_aleatoria"], show_sum=True, soma={
            "linhas": tabuleiro["somaLados"]["linhas"],
            "colunas": tabuleiro["somaLados"]["colunas"]
        })
        # print()
        funcoes.mostrar_matriz(tabuleiro["matriz_oculta"], funcoes.verificar_somas_matriz(tabuleiro["matriz_oculta"]))

        tipo = funcoes.receber_e_validar_entrada_tipo() # c = coluna; l = linha

        index = funcoes.receber_e_validar_entrada_col_row(tipo, N_COLS, N_LINHAS) -1 # -1 pois o usuario digita a partir do 1 e a matriz le a partir do 0

        soma = int(input("Digite o valor da soma: "))

        historico_jogadas["jogador1" if quemJoga == 0 else "jogador2"].append({
            "tipo": tipo,
            "index": index,
            "soma": soma
        })


        valor = []
        somaLado = 0

        if tipo == "c":
            valor = [tabuleiro["matriz_aleatoria"][i][index] for i in range(N_COLS)]
            somaLado = tabuleiro["somaLados"]["colunas"][index]
        else:
            valor = [tabuleiro["matriz_aleatoria"][index][i] for i in range(N_COLS)]
            somaLado = tabuleiro["somaLados"]["linhas"][index]

        if somaLado == soma:
            jaFoi = False

            somaDoUsuario = funcoes.verificar_somas_matriz(tabuleiro["matriz_oculta"])

            # verifica se a soma já foi feita
            if tipo == "c":
                if somaDoUsuario["colunas"][index] != 0:
                    jaFoi = True
            else:
                if somaDoUsuario["linhas"][index] != 0:
                    jaFoi = True
            
            if jaFoi: # se já foi feita
                print("Coluna já está completa!")
                print("Você não ganhou nenhum ponto.")
            else: # se ainda não foi feita
                if tipo == "c":
                    for i in range(N_COLS):
                        tabuleiro["matriz_oculta"][i][index] = valor[i]
                elif tipo == "l":
                    tabuleiro["matriz_oculta"][index] = valor
                print("Parabéns, você acertou a soma!")
                print("Você ganhou 3 pontos!")
                pontuacao["jogador1" if quemJoga == 0 else "jogador2"] += 3 # adiciona 3 pontos em caso de acertar tudo
        elif somaLado > soma:
            jaFoi = False
            x = y = maxValue = 0

            if tipo == "c":
                maxValue = min(valor)
                indexValue = valor.index(maxValue)
                x = indexValue
                y = index
            elif tipo == "l":
                maxValue = min(valor)
                indexValue = valor.index(maxValue)
                x = index
                y = indexValue
                
            if tabuleiro["matriz_oculta"][x][y] != "><": # se a posição já estiver preenchida
                jaFoi = True
                print("A soma é maior!")
                print("Como você não abriu uma casa nova, não ganhou ponto.")
            else:
                pontuacao["jogador1" if quemJoga == 0 else "jogador2"] += 1 # adiciona 1 ponto em caso de mostrar uma casa
                tabuleiro["matriz_oculta"][x][y] = maxValue
                print("A soma é maior!")
                print("Você ganhou 1 ponto por mostrar uma casa!")
        else:
            x = y = maxValue = 0
            if tipo == "c":
                maxValue = max(valor)
                indexValue = valor.index(maxValue)
                x = indexValue
                y = index
            elif tipo == "l":
                maxValue = max(valor)
                indexValue = valor.index(maxValue)
                x = index
                y = indexValue

            if tabuleiro["matriz_oculta"][x][y] != "><": # se a posição já estiver preenchida
                jaFoi = True
                print("A soma é menor!")
                print("Como você não abriu uma casa nova, não ganhou ponto.")
            else:
                pontuacao["jogador1" if quemJoga == 0 else "jogador2"] += 1 # adiciona 1 ponto em caso de mostrar uma casa
                tabuleiro["matriz_oculta"][x][y] = maxValue
                print("A soma é menor!")
                print("Você ganhou 1 ponto por mostrar uma casa!")

        # Verifica o próximo a jogar
        if quemJoga == 0: # se quem jogou foi o jogador 1
            quemJoga = 1 # proximo jogador = jogador2
        else: # se quem jogou foi o jogador 2
            quemJoga = 0 # proximo jogador = jogador1

        input("\nAperte enter para continuar:")

    funcoes.clear() # limpa a tela
    
    funcoes.animacao_inicio() # mostra a animação de inicio

    print("="*70)
    print("{:^50}".format("FIM DO JOGO!"))
    print("="*70)

    funcoes.clear() # limpa a tela

    if pontuacao["jogador1"] > pontuacao["jogador2"]:
        historico_jogadas["vencedor"] = "1"
        print("O jogador 1 venceu!")
    elif pontuacao["jogador1"] < pontuacao["jogador2"]:
        historico_jogadas["vencedor"] = "2"
        print("O jogador 2 venceu!")
    else:
        historico_jogadas["vencedor"] = "empate"
        print("Empate!")

    verHistorico = input("Deseja ver o histórico de jogadas? (s/n)")[0].lower() == "s"
    if verHistorico:
        funcoes.mostrar_historico(historico_jogadas)
if __name__ == "__main__":
    main()