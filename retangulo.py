'''
Programa: Imprime retangulo cheio
'''

# Principal
def main():

    # Tratamento de erro
    try:

        # Chamada de metodo + submetodo
        ret_vazado(lag(), alt())

    except:
        print("# Invalido")

# Metodo: Largura
def lag():

    # Entrada de dados
    lag = int(input("digite a largura: "))

    # Estrutura de repeticao: Protecao
    while lag <= 0:

        lag = int(input("digite a largura: "))

    return lag

# Metodo: Altura
def alt():

    # Entrada de dados
    alt = int(input("digite a altura: "))

    # Estrutura de repeticao: Protecao
    while alt <= 0:

        alt = int(input("digite a altura: "))

    return alt

# Metodo: Retangulo vazado
def ret_vazado(lag, alt):

    # Variavel
    i = 1

    # Estrutura de repeticao
    while i <= alt:

        # Estrutura de decisao
        if i == 1:  # 1ª linha
            print("#" * lag)

        elif i == alt:  # Ultima linha
            print("#" * lag)

        else:
            print("#", end="")
            print("#".rjust(lag - 1))  # Imprimindo aliando a direita

        # Incremento
        i += 1

# Execucao
if __name__ == '__main__':
    main()
