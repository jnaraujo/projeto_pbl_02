""" /*******************************************************************************

    Autor: Jônatas Araújo Silva Santos
    Componente Curricular: Algoritmos I
    Concluido em: 21/05/2022
    Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
    trecho de código de outro colega ou de outro autor, tais como provindos de livros e
    apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código de
    outra autoria que não a minha está destacado com uma citação para o autor e a fonte do
    código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

******************************************************************************************/ """

########## LIBS ##########

from utils import funcoes, tela

########## Variáveis ##########

N_COLS = 1 # Número de colunas do tabuleiro
N_LINHAS = 1 # Número de linhas do tabuleiro
QNT_RAND_NUNS = 1 # Quantidade de números aleatórios

# Armazena o historico de jogadas
historico_jogadas = {
    "jogador1": [],
    "jogador2": [],
    "vencedor": "",
}
# Armazena a pontuação de cada jogador
pontuacao = {
    "jogador1": 0,
    "jogador2": 0,
}
# Armazena o número máximo de rounds
max_rounds = 0

tipo_termino = "soma" # como o jogador desejar terminar o jogo; "soma" ou "round"


def main():
    tela.animacao_inicio()

    tela.clear()

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

    print("{:^70s}".format("Deseja ver as regras?:\n"))
    print("[0] {:<8} [1] {:<8}".format("Não", "Sim"))
    ver_regras = funcoes.receber_e_validar_entrada_numeros("", 0, 1)

    if ver_regras == 1:
        tela.mostrar_regras()
        input("Pressione ENTER para continuar...")
        tela.clear()


    ########## INICIALIZAÇÃO ##########

    # Modos do jogo

    print("{:^70s}".format("Modos de jogo:\n"))
 
    print("Quantos tabuleiros?")
    print("[0] {:<8} [1] {:<8}".format("Um tabuleiro", "Dois tabuleiros"))
    modo = funcoes.receber_e_validar_entrada_numeros("", 0, 1) # Recebe e valida o modo de jogo

    print("Qual o nível?")
    print("[0] {:<8} [1] {:<8} [2] {:<8}".format("Fácil (3x3)", "Médio (4x4)", "Difícil (5x5)"))
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
        "somaLados": [], # quanto vale a soma das colunas e linhas
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

    # VARIÁVEIS DE JOGO
    quemJoga = 0 # 0 = jogador1, 1 = jogador2
    contadorDeJogadas = 0 # contador de jogadas
    rodada = 0 # contador de rodadas
    playCount = 0

    deveAnalisarResultados = False # se deve analisar os resultados da aproximação

    while not funcoes.have_the_game_finished(tabuleiro1["matriz_oculta"], tabuleiro2["matriz_oculta"], rodada, max_rounds, tipo_termino): # enquanto não tiver todas as posições preenchidas
        tela.clear()

        playCount += 1
        if playCount == 3: # se for a segunda rodada
            deveAnalisarResultados = True # deve analisar os resultados da aproximação
            playCount = 0

        if deveAnalisarResultados == False: # se for uma partida válida
            tabuleiro = {}

            if modo == 1: # modo de 2 tabuleiros
                if quemJoga == 0:
                    tabuleiro = tabuleiro1
                else:
                    tabuleiro = tabuleiro2
            else:
                tabuleiro = tabuleiro1

            rodada = (contadorDeJogadas / 2) + 1 # contador de rodadas
            contadorDeJogadas += 1

            print("="*70)
            print("{:^70s}".format("Rodada {:.0f}".format(int(rodada))))
            print("{:^70s}".format("Quem joga: " + ("Jogador 1" if quemJoga == 0 else "Jogador 2")))
            print("{:^70s}".format("Jogador 1 | {} x {} | Jogador 2".format(pontuacao["jogador1"], pontuacao["jogador2"])))
            print("="*70)

            # tela.mostrar_matriz_com_resultados(tabuleiro["matriz_aleatoria"], show_sum=True, soma={
            #     "linhas": tabuleiro["somaLados"]["linhas"],
            #     "colunas": tabuleiro["somaLados"]["colunas"]
            # })
            
            tela.mostrar_matriz(tabuleiro["matriz_oculta"], funcoes.verificar_somas_matriz(tabuleiro["matriz_oculta"]))

            tela.mostrar_historico_parcial(historico_jogadas["jogador1" if quemJoga == 0 else "jogador2"])

            tipo = funcoes.receber_e_validar_entrada_tipo() # c = coluna; l = linha

            index = funcoes.receber_e_validar_entrada_col_row(tipo, N_COLS) -1 # -1 pois o usuario digita a partir do 1 e a matriz le a partir do 0

            soma = funcoes.receber_e_validar_entrada_numeros("Digite o valor da soma: ", 1, 99999)

            historico_jogadas["jogador1" if quemJoga == 0 else "jogador2"].append({
                "tipo": tipo,
                "index": index,
                "soma": soma,
                "resultado": -2
            })

            # Verifica o próximo a jogar
            if quemJoga == 0: # se quem jogou foi o jogador 1
                quemJoga = 1 # proximo jogador = jogador2
            else: # se quem jogou foi o jogador 2
                quemJoga = 0 # proximo jogador = jogador1
        else: # mostrar quem chegou mais perto da aproximação
            ultimaJogadaJogador1 = historico_jogadas["jogador1"][-1]
            ultimaJogadaJogador2 = historico_jogadas["jogador2"][-1]
 
            tabuleiro = [] # tabuleiro que será mostrado do jogador
            tipo = "" # se é coluna ou linha
            index = 0  # index da linha ou coluna
            soma = 0 # soma que o jogador digitou

            maisProximo = "empate"

            if modo == 1: # modo de 2 tabuleiros
                maisProximo = funcoes.pegarMaisProximo(historico_jogadas, tabuleiro1["matriz_aleatoria"], tabuleiro2["matriz_aleatoria"]) # pega quem está mais perto da aproximação
            else:
                maisProximo = funcoes.pegarMaisProximo(historico_jogadas, tabuleiro1["matriz_aleatoria"], tabuleiro1["matriz_aleatoria"]) # pega quem está mais perto da aproximação

            if maisProximo == "jogador1": # se o jogador 1 está mais perto da aproximação
                tabuleiro = tabuleiro1 # tabuleiro que será mostrado do jogador

                tipo = ultimaJogadaJogador1["tipo"] # se é coluna ou linha
                index = ultimaJogadaJogador1["index"] # index da linha ou coluna
                soma = ultimaJogadaJogador1["soma"] # soma que o jogador digitou

                print("="*70)
                print("{:^70s}".format("Jogador 1 chegou mais perto!"))
                print("="*70)

                resultado1 = funcoes.analisar_matriz(tabuleiro, index, tipo, soma, N_COLS)

                historico_jogadas["jogador1"][-1]["resultado"] = resultado1

                if resultado1 in [1,2]: # mostrou somente uma casa
                    print("O chute foi {} que a soma correta!".format("maior" if resultado1 == 1 else "menor"))
                    print("O jogador 1 mostrou somente 1 casa.")
                    print("O jogador 1 ganhou 1 ponto.")
                    funcoes.dar_pontos(0, 1, pontuacao) # dar 1 ponto ao jogador 1
                elif resultado1 == 0: # mostrou todas as casas
                    print("O jogador 1 mostrou todas as casas.")
                    print("O jogador 1 ganhou 3 ponto.")
                    funcoes.dar_pontos(0, 3, pontuacao) # dar 3 pontos ao jogador 1
                else:
                    print("A casa do jogador 1 já tinha sido mostrada.")
                    print("O jogador 1 ganhou 0 pontos.")
                
            elif maisProximo == "jogador2":
                if modo == 1: # modo de 2 tabuleiros
                    tabuleiro = tabuleiro2
                else:
                    tabuleiro = tabuleiro1

                tipo = ultimaJogadaJogador2["tipo"]
                index = ultimaJogadaJogador2["index"]
                soma = ultimaJogadaJogador2["soma"]

                print("="*70)
                print("{:^70s}".format("Jogador 2 chegou mais perto!"))
                print("="*70)

                resultado1 = funcoes.analisar_matriz(tabuleiro, index, tipo, soma, N_COLS)

                historico_jogadas["jogador2"][-1]["resultado"] = resultado1

                if resultado1 in [1,2]: # mostrou somente uma casa
                    print("O chute foi {} que a soma correta!".format("maior" if resultado1 == 1 else "menor"))
                    print("O jogador 2 mostrou somente 1 casa.")
                    print("O jogador 2 ganhou 1 ponto.")
                    funcoes.dar_pontos(1, 1, pontuacao)
                elif resultado1 == 0: # mostrou todas as casas
                    print("O jogador 2 mostrou todas as casas.")
                    print("O jogador 2 ganhou 3 ponto.")
                    funcoes.dar_pontos(1, 3, pontuacao)
                else:
                    print("A casa do jogador 2 já tinha sido mostrada.")
                    print("O jogador 2 ganhou 0 pontos.")
                
            else: # empate
                print("="*70)
                print("{:^70s}".format("Os dois jogadores chegaram perto da soma!"))
                print("="*70)

                tipo = ultimaJogadaJogador1["tipo"] # se é coluna ou linha
                index = ultimaJogadaJogador1["index"]
                soma = ultimaJogadaJogador1["soma"]

                tabuleiro = tabuleiro1

                resultado1 = funcoes.analisar_matriz(tabuleiro, index, tipo, soma, N_COLS)

                historico_jogadas["jogador1"][-1]["resultado"] = resultado1

                if resultado1 in [1,2]: # mostrou somente uma casa
                    print("O chute do jogador 1 foi {} que a soma correta!".format("maior" if resultado1 == 1 else "menor"))
                    print("O jogador 1 mostrou somente 1 casa.")
                    print("O jogador 1 ganhou 1 ponto.")
                    funcoes.dar_pontos(0, 1, pontuacao)
                elif resultado1 == 0: # mostrou todas as casas
                    print("O jogador 1 mostrou todas as casas.")
                    print("O jogador 1 ganhou 3 ponto.")
                    funcoes.dar_pontos(0, 3, pontuacao)
                else:
                    print("A casa do jogador 1 já tinha sido mostrada.")
                    print("O jogador 1 ganhou 0 pontos.")

                tipo = ultimaJogadaJogador2["tipo"] # se é coluna ou linha
                index = ultimaJogadaJogador2["index"]
                soma = ultimaJogadaJogador2["soma"]

                if modo == 1: # modo de 2 tabuleiros
                    tabuleiro = tabuleiro2

                resultado2 = funcoes.analisar_matriz(tabuleiro, index, tipo, soma, N_COLS)

                historico_jogadas["jogador2"][-1]["resultado"] = resultado2

                if resultado2 in [1,2]: # mostrou somente uma casa
                    print("O chute do jogador 2 foi {} que a soma correta!".format("maior" if resultado2 == 1 else "menor"))
                    print("O jogador 2 mostrou somente 1 casa.")
                    print("O jogador 2 ganhou 1 ponto.")
                    funcoes.dar_pontos(1, 1, pontuacao)
                elif resultado2 == 0: # mostrou todas as casas
                    print("O jogador 2 mostrou todas as casas.")
                    print("O jogador 2 ganhou 3 ponto.")
                    funcoes.dar_pontos(1, 3, pontuacao)
                else:
                    print("A casa do jogador 2 já estava tinha sido mostrada.")
                    print("O jogador 2 ganhou 0 pontos.")
                # tela.clear()
                
            deveAnalisarResultados = False
        input("\nAperte enter para continuar:")

    tela.clear() # limpa a tela
    
    tela.animacao_inicio() # mostra a animação de inicio

    tela.clear() # limpa a tela

    print("="*70)
    print("{:^70s}".format("FIM DO JOGO!"))
    print("="*70)

    

    if pontuacao["jogador1"] > pontuacao["jogador2"]:
        historico_jogadas["vencedor"] = "1"
        print("="*70)
        print("|{:^70s}|".format("Resultado: O jogador 1 venceu!"))
        print("="*70)
    elif pontuacao["jogador1"] < pontuacao["jogador2"]:
        historico_jogadas["vencedor"] = "2"
        print("="*70)
        print("{:^70s}".format("Resultado: O jogador 2 venceu!"))
        print("="*70)
    else:
        historico_jogadas["vencedor"] = "empate"
        print("="*70)
        print("{:^70s}".format("Resultado: EMMMMPATEE!"))
        print("="*70)
    
    print("\nObrigado por jogar!\n")

    verHistorico = input("Deseja ver o histórico de jogadas? (s/n)")[0].lower() == "s"
    if verHistorico:
        tela.mostrar_historico(historico_jogadas)

    # tela.clear() # limpa a tela

    print("="*70)
    print("{:^50}".format("FIM DO JOGO!"))
    print("{:^50}".format("Obrigado por jogar!"))
    print("="*70)


if __name__ == "__main__":
    main()