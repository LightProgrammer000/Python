# Biblioteca
import os

###########
# FUNCOES #
###########

def numerosPares():

    # Variaveis de controle
    j = 0

    # Apresentacao
    print(" # Numeros Pares")

    # Estrutura de repeticao: Numeros pares
    listaPares = []
    for  i in range(0, 50, 2):

        # Acrescentar na lista
        listaPares.append(i)

    # Saida de dados
    for i in range(0, len(listaPares)):

        if (j < 4):
            j += 1
            print("", listaPares[i], end="\t")

        else:
            j = 0
            print("", listaPares[i], end="\n")

def fatorial():

    # Variaveis de controle
    n = 5
    fat = 1
    listaFatorial = []

    # Apresentacao
    print("\n # Fatorial")

    # Estrutura de repreticao
    for i in range(1, n + 1):
        fat *= i
        listaFatorial.append(i)

    print(" # {} =".format(fat), end=" ")

    for i in range(1, len(listaFatorial)+1):

        if (i != len(listaFatorial)):
            print("", i, end=" *")

        else:
            print("", i, end="")

def progressaoAritmetica1():

    # Variaveis
    j = 0

    # Apresentacao
    print("\n\n # Progressao Aritmetica 1")

    # Estrutura de repeticao
    for i in range(1, 60, 2):

        if (j < 5):
            j += 1
            print("", i, end="\t")

        else:
            j = 0
            print("", i, end="\n")

def progressaoAritmetica2():

    # Controle
    n = 1
    listaAritmetica = []

    print("\n # Progressao Aritmetica 2")
    listaAritmetica.append(n)

    for i in range(0, 15):
        n *= 2
        listaAritmetica.append(n)

    for i in range(0, len(listaAritmetica)):
        print("", listaAritmetica[i], end=" ")

def progressaoGeometrica1():

    # Variaveis
    j = 0
    n = 1

    print("\n\n # Progressao Geometrica 1")
    for i in range(1, 7):
        n *= 2

        if (j < 2):
            print("", n, end="\t")
            j += 1

        else:
            print("", n, end="\n")
            j= 0

def progressaoGeometrica2():

    # Estrutura de repeticao: Progressao aritmetica
    n = 1
    listaGeometrica = []

    for i in range(1, 20):
        n *= 2
        listaGeometrica.append(n)

    print("\n # Progressao Geometrica 2")
    for i in listaGeometrica:
        print("", i, end=" ")

# Principal
def main():

    # Sistema
    os.system("clear")

    # Apresentacao
    print("\n\033[01;36m {} Programa 13 {}\n\033[01;37m".format("=-=" * 5, "=-=" * 5))

    # Numeros pares
    numerosPares()

    # Fatorial
    fatorial()

    # Progressao Aritmetica
    progressaoAritmetica1()
    progressaoAritmetica2()

    # Progressao Geometrica
    progressaoGeometrica1()
    progressaoGeometrica2()

# Execucao
if __name__ == '__main__':
    main()
