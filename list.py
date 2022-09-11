# Exercicio:
# Crie uma funcao que adicione nomes de pessoas a uma lista, atraves de entrada no console,
# e apos inserir 5 nomes chame outra funcao que imprima todos os nomes desta lista
#
# Biblioteca
import os

##########
# FUNCAO #
##########

# Dados
def dados():

    # Controle
    i = 1
    lista = []

    while i < 6:
        lista.append(input(" {}) {}: ".format(i,"Nome")))
        i += 1

    return lista

# Impressao do relatorio
def relatorioLista(lista):

    print(" # {}".format("Relatorio"))

    for i in lista:
        print(" # Nome: {}".format(i))

def main():

    # Sistema
    os.system("clear")

    # Apresentacao
    print("\n\033[01;36m {} Programa 19 {}\n\033[01;37m".format("=-=" * 5, "=-=" * 5))

    relatorioLista(dados())

if __name__ == '__main__':
    main()
