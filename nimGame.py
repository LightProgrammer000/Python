'''
Programa: Jogo do NIM

Campeonato:
[1] n = 3 // m = 1
[2] n = 3 // m = 2
[3] n = 4 // m = 3
'''

# Metodo: Menu
def menu():

    # Apresentacao
    print("\nBem-vindo ao jogo do NIM! Escolha:")
    print("# 1 -> Partida isolada")
    print("# 2 -> Campeonato")
    opc = int(input("# Opc: "))

    # Estrutura de decisao: Partida
    if opc == 1:
        return 1

    # Estrutura de decisao: Campeonato
    elif opc == 2:
        return 2

    # Estrutura de decisao: Erro
    else:
        return 0

# Metodo: Partida
def partida():

    # Entrada de dados
    n = int(input("Quantas peças? "))  # Obs: n o número de peças inicial
    n = protecao_pecas(n)

    m = int(input("Limite de peças por jogada? "))  # Obs: m o número máximo de peças que é possível retirar em uma rodada
    m = protecao_limites(m)

    # Estrutura de decisao: Logica
    # Exemplo: n = 4 -- m = 3
    if (n % (m + 1)) == 0:

        # Apresentacao
        print("\nVoce começa!")

        # Estrutura de repeticao: Numero de peças nao chegou a 'zero'
        while n > 0:

            # Chamada de metodo: Jogada do usuario
            b = usuario_escolhe_jogada(n, m)
            print(acerto_texto_jogador(b))

            # Calculo: Numero de pecas atual
            n -= b
            print(acerto_texto_peca(n))

            # Chamada de metodo: Jogada do computador
            a = computador_escolhe_jogada(n, m)
            print(acerto_texto_computador(a))

            # Calculo: Numero de pecas atual
            n -= a
            print(final_jogo(n))

    # Exemplo: n = 6 -- m = 3
    else:

        # Apresentacao
        print("\nComputador começa!")

        # Estrutura de repeticao: Numero de peças
        while n > 0:

            # Calculo
            a = computador_escolhe_jogada(n, m)
            print(acerto_texto_computador(a))

            # Calculo: Numero de peças
            n -= a

            # Estrutura de decisao: Nenhuma peça
            if n == 0:
                print("Fim do jogo! O computador ganhou!")

            # Estrutura de decisao:
            else:
                print("Agora restam", n, "peças no tabuleiro.")

                b = usuario_escolhe_jogada(n, m)
                print(acerto_texto_jogador(b))

                # Calculo: Numero de peças
                n -= b
                print(acerto_texto_peca(n))

####### Metodo de controle geral #######
def acerto_texto_computador(a):

    # Estrutura de decisao: Acerto do texto
    if a > 1:
        return "\nO computador tirou " + str(a) + " peças."

    else:
        return "\nO computador tirou uma peça."

def acerto_texto_jogador(b):

    # Estrutura de decisao: Acerto do texto
    if b > 1:
        return "Você tirou " + str(b) + " peças."

    else:
        return "Você tirou uma peça."

def acerto_texto_peca(n):

    # Estrutura de decisao: Acerto do texto
    if n > 1:
        return "Agora restam " + str(n) + " peças no tabuleiro."

    else:
        return "Agora resta apenas uma peça no tabuleiro."

def final_jogo(n):

    # Estrutura de decisao: Acerto do texto + Final de jogo
    if n == 0:
        return "Fim do jogo! O computador ganhou!"

    elif n == 1:
        return "Agora restam apenas uma peça no tabuleiro."

    else:
        return "Agora restam " + str(n) + " peças no tabuleiro."

####### Metodo de protecao #######
def protecao_pecas(n):

    while n <= 0:
        print("\nInvalido")
        n = int(input("Quantas peças? "))

    return n

def protecao_limites(m):

    while m <= 0:
        print("\nInvalido")
        m = int(input("Limite de peças por jogada? "))

    return m

# Metodo: Campeonato
def campeonato():

    # Variavel
    rodada = 1

    # Estrutura de repeticao
    while rodada < 4:

        # Apresentacao
        print("\n**** Rodada", rodada, "****\n")

        # Chamada de metodo
        partida()

        # Incremento
        rodada += 1

    # Apresentacao
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você 0 X 3 Computador")

# Metodo: Jogada do computador
def computador_escolhe_jogada(n, m):

    # Variavel: Controle de retirada de pecas pelo computador
    comp_ret = 0

    # Estrutura de repeticao: Pecas > Retiradas pelo computador
    while m >= comp_ret:

        if (n - comp_ret) % (m + 1) == 0:
            return comp_ret

        comp_ret += 1

    return m

# Metodo: Jogada do usuario
def usuario_escolhe_jogada(n, m):

    # Entrada de dados
    usu = int(input("\nQuantas peças você vai tirar? "))

    # Estrutura de repeticao: (Jogada do usuario > limite) ou (Jogada do usuario > numero de pecas)
    while (usu > m) or (usu > n) or (usu <= 0):

        # Apresentacao
        print("\nOops! Jogada inválida! Tente de novo.")

        # Entrada de dados
        usu = int(input("\nQuantas peças você vai tirar? "))

    return usu

# Programa principal
def main():

    # Chamada de metodo
    opc = menu()

    # Estrutura de decisao: Menu (Partida)
    if opc == 1:

        print("Voce escolheu uma partida isolada!\n")
        partida()

    # Estrutura de decisao: Menu (Campeonato)
    elif opc == 2:

        print("Voce escolheu um campeonato!")
        campeonato()

    else:
        exit(0)

# Execucao
if __name__ == '__main__':
    main()
