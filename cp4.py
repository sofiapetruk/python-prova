def incializarTabuleiro(n_linhas, n_colunas):
    # matriz_princial = []
    # for i in range(n_linhas):
    #     linha = []  #criar outra lista para criar uma matriz de linha, depois colocar na matriz
    #     for j in range(n_colunas):
    #     colunas = []    
    #     matriz_princial.append(linha,colunas) # fora do primeiro for pq ele só adiciona a coluna
    # return matriz_princial
    matriz = [{0 for i in range (3)},{0 for j in range (3)}]
    
    for linha in range (3):
        for coluna in range(3):
            count = 0
            matriz= [linha] [coluna] = count
            count += 1
        print (matriz)






def imprimirTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        posicao = ""
        for j in range(len(tabuleiro)):
            posicao = "" 
        print(posicao)






def imprimirMenuPrincipal():






def leiaCoordenadaLinha():






def imprimePontuacao():






def posicaoValida():
    if tabuleiro[linha][coluna] != ' ':
                print("Essa posição já está ocupada. Tente novamente.")
                continue





def verificaVencedor():





def verificaVelha():






def modoJogador():






def modoFacil():






def modoDificil():






def jogadaUsuario():







def jogadaMaquinaFacil():





def jogadaMaquinaDificil():
