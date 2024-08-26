def incializarTabuleiro():
    matriz = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]
    
    return matriz

def imprimirTabuleiro(matriz):
    """for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(f"[{linha}][{coluna}]")"""
    print(matriz)
  



#https://dev.to/iugstav/python-manipulacao-de-listas-e-matrizes-4bpj
#https://awari.com.br/como-criar-e-manipular-matrizes-em-python-guia-completo-para-iniciantes/

#Principal
matriz = incializarTabuleiro()
imprimirTabuleiro(matriz)


