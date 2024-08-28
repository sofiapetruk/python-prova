def incializarTabuleiro():
    matriz_princiapal = []
    soma = 0
    for linha in range(3):
        linha = []
        for coluna in range(3):
            linha.append(soma)
            soma += 1
        matriz_princiapal.append(linha)
    return matriz_princiapal

def imprimirMatriz(matriz_principal):
    for linha in matriz_principal:
        print(" | ".join(str(x) for x in linha))
        print("-" * 9)
    




#Princiapal
matriz_principal = incializarTabuleiro()
imprimirMatriz(matriz_principal)

