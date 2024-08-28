def inicializarTabuleiro():
    return [[' ' for i in range(3)] for j in range(3)]

def imprimirtabuleiro(matriz):
    for i in matriz:
        print(i)
        print("---------------")

matriz = inicializarTabuleiro()
imprimirtabuleiro(matriz)

def imprimirMenuPrincipal():
    print(f"""          
          +----------------------------------+
           (1) = Jogador X Jogador
           (2) = Jogador X Máquina(Fácil)
           (3) = Jogador X Máquina(Difícil)
          +----------------------------------+
          """)
    escolha = int(input("-- Escolha o número correspondente ao modo de jogo que desejar jogar: "))
    if escolha < 1 or escolha > 3:
        print("Escolha inválida") 
imprimirMenuPrincipal()

def posicao_valida(matriz):
    result = []
    for i in range(3):
        for j in range(3):
            if (matriz[i][j] == ""):
                result.append((i, j))
    return result

def leia_coordenada(matriz):
    posicoes_disponiveis = posicao_valida(matriz)
    while True:
        i = int(input("Insira o número da linha (0-3): "))
        j = int(input("Insira o número da coluna (0-3): "))
        if (i, j) in posicoes_disponiveis:
            return (i, j)
        print("Posição já ocupada ou inválida")

def verifica_vencedor(matriz):
    for i in range (3): #Para linha
        if matriz[i][0] == 'X' and matriz[i][1] == 'X' and matriz[i][2] == 'X':
            print('Jogador 1 Ganhou!')
            return True
        
    if matriz[i][0] == 'O' and matriz[i][1] == 'O' and matriz[i][2]== 'O':
                print('Jogador 2 Ganhou!')
                return True
        
    for j in range (3): #Para coluna
            if matriz[0][j] == 'X' and matriz[1][j] == 'X' and matriz[2][j] == 'X' :
                print('Jogador 1 Ganhou!')
                return True
 
    if matriz[0][j] == 'O' and matriz[1][j] == 'O' and matriz[2][j] == 'O' :
            print('Jogador 2 Ganhou!')        
            return True
    
    if matriz[0][0]== 'X' and matriz[1][1]== 'X' and matriz[2][2] == 'X':
        print ('Jogador 1 Ganhou!')
        return True
          
    if matriz[0][2]== 'X' and matriz[1][1]== 'X' and matriz[2][0] == 'X':
        print ('Jogador 1 Ganhou!')
        return True
                  
    if matriz[0][0]== 'O' and matriz[1][1]== 'O' and matriz[2][2] == "O":
        print ('Jogador 2 Ganhou!')
        return True
          
    if matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O':
        print('Jogador 2 Ganhou!')
        return True
        
    return False

def verifica_velha(matriz):
    if len(posicao_valida(matriz)) == 0:
        return True
    return False