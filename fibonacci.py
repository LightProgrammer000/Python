"""
# Exercicio
# Crie uma funcao que imprima a sequencia de Fibonacci
# Ex: 1, 1, 2, 3, 5, 8, 13, 21, 34
"""
# Biblioteca
import os

def dados():
    return int(input(" # Quantidade de numeros: "))

def fibonacci(qtd):

    # Controle
    cont = 0
    lista = []

    # Variaveis
    a = 1
    b = 1

    while cont < qtd:

        lista.append(a)
        a += b
        cont += 1

        # Controle de loop
        if cont == qtd:
            break

        else:
            lista.append(b)
            b += a
            cont += 1

    return lista

def main():

    # Sistema
    os.system("clear")

    # Apresentacao
    print("\n\033[01;36m {} Programa 17 {}\n\033[01;37m".format("=-=" * 5, "=-=" * 5))

    # Incrementando na lista nova
    listaNova = fibonacci(dados())

    print("\033[01;34m {} \033[01;37m".format("Sequencia: "))

    # Controle
    j = 0
    for i in range(0, len(listaNova)):

        if j < 3:
            print("\033[01;34m {}\033[01;37m".format(listaNova[i]), end=" ")
            j +=1

        else:
            print("\033[01;34m {}\033[01;37m".format(listaNova[i]), end="\n")
            j = 0

# Executar
if __name__ == '__main__':
    main()
