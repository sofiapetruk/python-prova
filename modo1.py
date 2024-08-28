def incializarTabuleiro():
    matriz = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
        ]
    
    return matriz

def imprimirTabuleiro(matriz): 
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            print(matriz[0])
            print(matriz[1])
            print(matriz[2])


def escolhaJogador(matriz):
    jogador1 = int(input('Escolha um número para colocar o X: '))
    matriz[jogador1-1] = "X"
    print(matriz)
    jogador2 = int(input('Escolha um número para colocar o O'))
    matriz[jogador2-1] = "O"
    return jogador1, jogador2
    



#Principal
matriz = incializarTabuleiro()
imprimirTabuleiro(matriz)
jogador1, jogador2 = escolhaJogador(matriz)


