# Biblioteca
import os

# Dados: Retornando somatorio dos pontos
def dados():

    # Controle
    pontos = 0
    listaPontos = []

    # Entrada de dados
    print("\033[01;31m {} Tomara que Caia {}\033[01;37m".format("=-=" * 6, "=-=" * 6))

    a1 = int(input("\033[01;32m\n - Qual cor voce mais o acalma: \n 1. Preto \n 2. Vermelho \n 3. Azul \n 4. Rosa \n # Resp: \033[01;37m"))
    listaPontos.append(a1)

    a2 = int(input("\033[01;33m\n - Qual sabor voce mais gosta: \n 1. Doce \n 2. Salgado \n 3. Azedo \n 4. Acido \n # Resp: \033[01;37m"))
    listaPontos.append(a2)

    a3 = int(input("\033[01;34m\n - Qual geometria voce mais entende: \n 1. Triangulo \n 2. Circulo \n 3. Quadrado \n 4. Losango \n # Resp: \033[01;37m"))
    listaPontos.append(a3)

    a4 = int(input("\033[01;35m\n - Qual esporte voce mais divertido: \n 1. Natacao \n 2. Judo \n 3. Basquete \n 4. Futebol \n # Resp: \033[01;37m"))
    listaPontos.append(a4)

    a5 = int(input("\033[01;36m\n - Qual seu espectro politico: \n 1. Esquerda \n 2. Direita \n 3. Centro \n 4. Nenhum \n # Resp: \033[01;37m"))
    listaPontos.append(a5)

    for i in range(0, len(listaPontos)):
        pontos += listaPontos[i]

    return pontos

# Conferencia da pontuacao
def relatorio(pontos):

    # Resultado geral
    print("\033[01;31m\n {} Relatorio {}\n\033[01;37m".format("---" * 5, "---" * 5))

    # Lista de participantesss {dicionario}
    listaPaticipantes = { "H": "Heloisa Perisse",
                          "E": "Eri Johnson",
                          "R": "Ricardo Tozzi",
                          "M": "Monica Iozzi"
                        }

    # Participantes
    print(" # Lista de participantes: ")

    for i in listaPaticipantes:
        print(" * ", listaPaticipantes[i], end=" ")

    print("\n\n # Resultado: ", end="")

    # Estrutura de condicao
    if 20 >= pontos > 15:
        print("\033[01;32m {} \033[01;37m".format(listaPaticipantes["H"]))

    elif 15 >= pontos > 10:
        print("\033[01;32m {} \033[01;37m".format(listaPaticipantes["E"]))

    elif 10 >= pontos > 5:
        print("\033[01;32m {} \033[01;37m".format(listaPaticipantes["R"]))

    else:
        print("\033[01;32m {} \033[01;37m".format(listaPaticipantes["M"]))

# Principal
def main():

    # Sistema
    os.system("clear")

    # Apresentacao
    print("\n\033[01;36m {} Programa 06 {}\n\033[01;37m".format("=-=" * 5, "=-=" * 5))

    # Chamada de funcao
    relatorio(dados())

# Execucao
if __name__ == '__main__':
    main()
