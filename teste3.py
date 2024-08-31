def imprimeMenuPrincipal():
    opcao = -1
    while opcao < 1 or opcao > 3:
        print(f"""\033[36m      
        +----------------------------------+
        (1) Jogador x Jogador
        (2) Jogador x Máquina nível fácil
        (3) Jogador x Máquina nível difícil
        +----------------------------------+\033[0m
        """)
        opcao = int(input("Digite o modo de jogo que você deseja: "))
        if opcao < 1 or opcao > 3:
            print("Opção inválida, tente novamente")
    return opcao

# Inicializa a pontuação dos jogadores
pontuacao = {'Jogador1': 0, 'Jogador2': 0}


def inicializarTabuleiro():
    matriz =  [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return matriz


def imprimir_tabuleiro(matriz):
    print("  0   1   2  ")
    print("┌───┬───┬───┐")  
    for linha in range(3):
        print("│ " + " │ ".join(matriz[linha]) + " │")
        if linha < 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")


def leiaCoordernadaLinha():
    linha = int(input("Escolha uma LINHA de 0 a 2 para colocar a sua peça: "))
    return linha


def leiaCoordernadoraColuna():
    coluna = int(input("Escolha uma COLUNA de 0 a 2 para colocar a sua peça: "))
    return coluna


def imprimePontuação(): #muda as classes para o _ quando mudar de palavra
    print("Pontuação de cada jogador:")
    print(f"Jogador 1 {pontuacao["Jogador1"]} pontos")
    print(f"Jogador 2 {pontuacao['Jogador2']} pontos") #depois mudar essa parte pq está parecida com o manoke


def posicaoValida(coluna, linha,matriz):
    if 0 <= linha < 3 and 0 <= coluna < 3:
        if matriz[linha][coluna] not in ["X", "O"]:
            return True
        else:
            print("A posição já está ocupada, tente novamente")
            return False
    else:
        print("Coordenada inválida tente novamente")
        return False
    

def verificaVencedor(matriz):
    """for linha in matriz:
        if linha[0] == linha[1] and linha[2] == "X": #tem que fazer a pontuação do joagador aqui
            print("O primeiro jogador ganhou")
            return True
        if linha[0] == linha[1] and linha[2] == "O":
            print("O segundo jogador ganhou")
            return True
        

    for coluna in matriz:
            if linha[0][coluna] == linha[1][coluna] and linha[2][coluna] == "X": #tem que fazer a pontuação do joagador aqui
                print("O primeiro jogador ganhou")
                return True
            if linha[0][coluna] == linha[1][coluna] and linha[2][coluna] == "O":
                print("O segundo jogador ganhou")
                return True
            
    
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == "X":
        print("O primeiro jogador ganhou")
        return True
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == "O":
        print("O segundo jogador ganhou")
        return True
    

    if matriz[0][2] == matriz[1][1] == matriz[2][0] == "X":
        print("O primeiro jogador ganhou")
        return True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] == "O":
        print("O segundo jogador ganhou")
        return True"""
    for linha in matriz:
        if linha[0] == linha[1] == linha[2]:
            if linha[0] == "X":
                return "Jogador1"
            elif linha[0] == "O":
                return "Jogador2"

    for coluna in range(3):
        if matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna]:
            if matriz[0][coluna] == "X":
                return "Jogador1"
            elif matriz[0][coluna] == "O":
                return "Jogador2"

    if matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[0][0] == "X":
            return "Jogador1"
        elif matriz[0][0] == "O":
            return "Jogador2"

    if matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[0][2] == "X":
            return "Jogador1"
        elif matriz[0][2] == "O":
            return "Jogador2"

    return None


def verificarVelha(matriz):
    """if len(posicaoValida(matriz)) == 0: #igual do manoke mudar
        return True
    return False""" 
    for linha in matriz:  #pego do chat gpt, pq o de cima não estava funcionando
        for cell in linha:
            if cell not in ["X", "O"]:
                return False
    return True

def modoJogador():
    matriz = inicializarTabuleiro()
    jogador_atual = "X" #mudar essa parte, pq quero que apreça como Jogador 1 e Jogador 2
    jogo = False

    while not jogo:
        imprimir_tabuleiro(matriz)
        print(f"Vez do jogador {jogador_atual}: ({jogador_atual})")

        linha = leiaCoordernadaLinha()
        coluna = leiaCoordernadoraColuna()

        while not posicaoValida(coluna, linha, matriz):
            linha = leiaCoordernadaLinha()
            coluna = leiaCoordernadoraColuna()

        matriz[linha][coluna] = jogador_atual

        vencedor = verificaVencedor(matriz)

        if vencedor:
            imprimir_tabuleiro(matriz)
            print(f"Jogador {vencedor} ganhou!")
            if vencedor == "X":
                pontuacao['Jogador1'] += 1
            else:
                pontuacao['Jogador2'] += 1
            imprimePontuação()
            jogo = True

        elif verificarVelha(matriz):
            imprimir_tabuleiro(matriz)
            print("O jogo terminou em empate")
            imprimePontuação
            jogo = True
        
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X" #mudar essa parte, pq quero que apreça como Jogador 1 e Jogador 2

# Principal
opcao = imprimeMenuPrincipal()
modoJogador()




