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
historico_jogadas = {
    "jogador1": [],
    "jogador2": [],
    "vencedor": "",
}
pontuacao = {
    "jogador1": 0,
    "jogador2": 0,
}

def clear():
    os.system("clear")

def main():

    # funcoes.animacao_inicio()

    funcoes.clear()

    print("="*50)
    print("{:^50s}".format("Bem vindo ao:"))
    print("{:^50s}".format("Jogo das Somas Esquecidas"))
    print("="*50)

    print()

    print("{:^50s}".format("Modos de jogo:\n"))

    print("Quantos tabuleiros?")
    print("[0] {:<8} [1] {:<8}".format("Um tabuleiro", "Dois tabuleiros"))

    modo = funcoes.receber_e_validar_entrada_numeros("", 0, 1)

    print("Qual o nível?")
    print("[0] {:<8} [1] {:<8} [2] {:<8}".format("Fácil", "Médio", "Difícil"))
    nivel = funcoes.receber_e_validar_entrada_numeros("", 0, 2)



    N_COLS = 1
    N_LINHAS = 1
    QNT_RAND_NUNS = 1


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
        "matriz_aleatoria": funcoes.gerar_matriz_aleatoria(N_LINHAS, N_COLS, QNT_RAND_NUNS),
        "matriz_oculta": funcoes.gerar_matriz_oculta(N_LINHAS, N_COLS),
        "somaLados": [],
        "rawSoma": {
            "linhas": [0] * N_LINHAS,
            "colunas": [0] * N_COLS
        }
    }
    tabuleiro1["somaLados"] = funcoes.somarLadosMatriz(tabuleiro1["matriz_aleatoria"])

    # TABULEIRO 2
    tabuleiro2 = {
        "matriz_aleatoria": funcoes.gerar_matriz_aleatoria(N_LINHAS, N_COLS, QNT_RAND_NUNS),
        "matriz_oculta": funcoes.gerar_matriz_oculta(N_LINHAS, N_COLS),
        "somaLados": [],
        "rawSoma": {
            "linhas": [0] * N_LINHAS,
            "colunas": [0] * N_COLS
        }
    }
    tabuleiro2["somaLados"] = funcoes.somarLadosMatriz(tabuleiro2["matriz_aleatoria"])

    #################################

    # }

    quemJoga = 0 # 0 = jogador1, 1 = jogador2
    # historico_jogadas
    rodada = 0 # contador de rodadas

    while funcoes.isMatrizCompleta(tabuleiro1["matriz_oculta"]) == False or funcoes.isMatrizCompleta(tabuleiro2["matriz_oculta"]): # enquanto não tiver todas as posições preenchidas
        clear()
        
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

        print("="*50)
        print("{:^50s}".format("Rodada {:.0f}".format(rodada-1)))
        print("{:^50s}".format("Quem joga: " + ("Jogador 1" if quemJoga == 0 else "Jogador 2")))
        print("{:^50s}".format("Jogador 1 | {} x {} | Jogador 2".format(pontuacao["jogador1"], pontuacao["jogador2"])))
        print("="*50)

        funcoes.mostrar_matriz_com_resultados(tabuleiro["matriz_aleatoria"], show_sum=True, soma={
            "linhas": tabuleiro["somaLados"]["linhas"],
            "colunas": tabuleiro["somaLados"]["colunas"]
        })
        # print()
        funcoes.mostrar_matriz(tabuleiro["matriz_oculta"], tabuleiro["rawSoma"])

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
            if tipo == "c":
                tabuleiro["rawSoma"]["colunas"][index] = soma
                for i in range(N_COLS):
                    tabuleiro["matriz_oculta"][i][index] = valor[i]
            elif tipo == "l":
                tabuleiro["rawSoma"]["linhas"][index] = soma
                tabuleiro["matriz_oculta"][index] = valor
            
            pontuacao["jogador1" if quemJoga == 0 else "jogador2"] += 3 # adiciona 3 pontos em caso de acertar tudo

            print("Parabéns, você acertou a soma!")
        elif somaLado > soma:
            if tipo == "c":
                maxValue = min(valor)
                indexValue = valor.index(maxValue)
                tabuleiro["matriz_oculta"][indexValue][index] = maxValue
            elif tipo == "l":
                maxValue = min(valor)
                indexValue = valor.index(maxValue)
                tabuleiro["matriz_oculta"][index][indexValue] = maxValue

            pontuacao["jogador1" if quemJoga == 0 else "jogador2"] += 1 # adiciona 1 ponto em caso de mostrar uma casa

            print("Você errou, a soma é maior!")
        else:
            if tipo == "c":
                maxValue = max(valor)
                indexValue = valor.index(maxValue)
                tabuleiro["matriz_oculta"][indexValue][index] = maxValue
            elif tipo == "l":
                maxValue = max(valor)
                indexValue = valor.index(maxValue)
                tabuleiro["matriz_oculta"][index][indexValue] = maxValue

            pontuacao["jogador1" if quemJoga == 0 else "jogador2"] += 1 # adiciona 1 pontos em caso de mostrar uma casa
            print("Você errou, a soma é menor!")


        # Verifica o próximo a jogar
        if quemJoga == 0: # se quem jogou foi o jogador 1
            quemJoga = 1 # proximo jogador = jogador2
        else: # se quem jogou foi o jogador 2
            quemJoga = 0 # proximo jogador = jogador1

        input("\nAperte enter para continuar:")

    funcoes.clear() # limpa a tela
    
    funcoes.animacao_inicio() # mostra a animação de inicio

    print("="*50)
    print("{:^50}".format("FIM DO JOGO!"))
    print("="*50)

    funcoes.clear() # limpa a tela

    if quemJoga == 0:
        historico_jogadas["vencedor"] = "2"
        print("O jogador 2 venceu!")
    elif quemJoga == 1:
        historico_jogadas["vencedor"] = "1"
        print("O jogador 1 venceu!")
    else:
        historico_jogadas["vencedor"] = "empate"
        print("Empate!")

    verHistorico = input("Deseja ver o histórico de jogadas? (s/n)")[0].lower() == "s"
    if verHistorico:
        funcoes.mostrar_historico(historico_jogadas)
if __name__ == "__main__":
    main()