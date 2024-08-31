# Função para imprimir o menu principal
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

# Inicializa o tabuleiro com números de 1 a 9
def inicializarTabuleiro():
    return [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

# Imprime o tabuleiro do jogo da velha
def imprimir_tabuleiro(matriz):
    print("┌───┬───┬───┐")  
    for linha in range(3):
        print("│ " + " │ ".join(matriz[linha]) + " │")
        if linha < 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")

# Lê a coordenada da linha do jogador
def leiaCoordernadaLinha():
    linha = int(input("Escolha uma LINHA de 0 a 2 para colocar a sua peça: "))
    return linha

# Lê a coordenada da coluna do jogador
def leiaCoordernadoraColuna():
    coluna = int(input("Escolha uma COLUNA de 0 a 2 para colocar a sua peça: "))
    return coluna

# Imprime a pontuação de cada jogador
def imprimePontuacao(): 
    print("Pontuação de cada jogador:")
    print(f"Jogador 1: {pontuacao['Jogador1']} pontos")
    print(f"Jogador 2: {pontuacao['Jogador2']} pontos")

# Verifica se a posição é válida e atualiza o tabuleiro se for o caso
def posicaoValida(coluna, linha, matriz):
    if 0 <= linha < 3 and 0 <= coluna < 3:
        if matriz[linha][coluna] not in ["X", "O"]:
            return True
        else:
            print("A posição já está ocupada. Tente novamente.")
            return False
    else:
        print("Coordenada inválida. Tente novamente.")
        return False

# Verifica se há um vencedor no tabuleiro
def verificaVencedor(matriz):
    # Verificar linhas
    for linha in matriz:
        if linha[0] == linha[1] == linha[2] and linha[0] in ["X", "O"]:
            return linha[0]
    
    # Verificar colunas
    for coluna in range(3):
        if matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna] and matriz[0][coluna] in ["X", "O"]:
            return matriz[0][coluna]
    
    # Verificar diagonais
    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] in ["X", "O"]:
        return matriz[0][0]
    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] in ["X", "O"]:
        return matriz[0][2]
    
    return None  # Nenhum vencedor ainda

# Verifica se o jogo terminou em empate
def verificarEmpate(matriz):
    for linha in matriz:
        for cell in linha:
            if cell not in ["X", "O"]:
                return False
    return True

# Função principal para o modo Jogador x Jogador
def modoJogador():
    matriz = inicializarTabuleiro()
    jogador_atual = "X"
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
            imprimePontuacao()
            jogo = True
        elif verificarEmpate(matriz):
            imprimir_tabuleiro(matriz)
            print("O jogo terminou em empate!")
            imprimePontuacao()
            jogo = True
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"

# Principal
opcao = imprimeMenuPrincipal()
modoJogador()
