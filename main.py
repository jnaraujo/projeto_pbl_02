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



def clear():
    os.system("clear")


N_COLS = 5
N_LINHAS = 5
QNT_RAND_NUNS = 100

matriz_aleatoria = funcoes.gerar_matriz_aleatoria(N_LINHAS, N_COLS, QNT_RAND_NUNS)
matriz_oculta = funcoes.gerar_matriz_oculta(N_LINHAS, N_COLS)
somaLados = funcoes.somarLadosMatriz(matriz_aleatoria)
# rawSoma = {
#     "linhas": [0] * N_LINHAS,
#     "colunas": [0] * N_COLS
# }
rawSoma = {
    "linhas": somaLados,
    "colunas": [0] * N_COLS
}

# matriz.mostrar_matriz(m, show_sum=True)
# matriz.mostrar_matriz_oculta(4,4)

while True:
    clear()

    funcoes.mostrar_matriz(matriz_aleatoria, show_sum=True, soma={
        "linhas": somaLados["linhas"],
        "colunas": somaLados["colunas"]
    })
    # print()
    funcoes.mostrar_matriz2(matriz_oculta, rawSoma)

    tipo = input("Digite o tipo de soma: (c)oluna ou (l)inha: ")[0].lower() # c = coluna; l = linha
    index = int(input("Digite o lado da {}: ".format("coluna" if tipo == "c" else "linha")))-1
    soma = int(input("Digite o valor da soma: "))
    valor = []
    if tipo == "c":
        valor = [matriz_aleatoria[i][index] for i in range(N_COLS)]
    else:
        valor = [matriz_aleatoria[index][i] for i in range(N_COLS)]

    somaLado = somaLados["colunas"][index]

    if somaLado == soma:
        if tipo == "c":
            rawSoma["colunas"][index] = soma
            for i in range(N_COLS):
                matriz_oculta[i][index] = valor[i]
        elif tipo == "l":
            rawSoma["linhas"][index] = soma
            matriz_oculta[index] = valor
        print("Parabéns, você acertou a soma!")
    elif somaLado > soma:
        if tipo == "c":
            maxValue = min(valor)
            indexValue = valor.index(maxValue)
            matriz_oculta[indexValue][index] = maxValue
        elif tipo == "l":
            maxValue = min(valor)
            indexValue = valor.index(maxValue)
            matriz_oculta[index][indexValue] = maxValue
        print("Você errou, a soma é maior!")
    else:
        if tipo == "c":
            maxValue = max(valor)
            indexValue = valor.index(maxValue)
            matriz_oculta[indexValue][index] = maxValue
        elif tipo == "l":
            maxValue = max(valor)
            indexValue = valor.index(maxValue)
            matriz_oculta[index][indexValue] = maxValue
        print("Você errou, a soma é menor!")

    input("\nAperte enter para continuar:")