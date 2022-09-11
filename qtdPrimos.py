'''
Programa 14: Quantidade de numeros primos
'''

def main():

    i = 1
    qtd = 0
    lim = int(input("# Limite de numeros primos: "))

    # Estrutura de repeticao
    while i > 0:

        # Chamada de metodo
        a = primo(i)

        # Estrutura de decisao
        if a != 0 and qtd != lim:

            # Apresentacao
            print("{}: {}".format(qtd + 1, a))

            # Incremento de contagem
            qtd += 1

        elif qtd == lim:
            break

        # Incremento
        i += 1

# Metodo: Verificacao do umero primo
def primo(num):

    # Variaveis
    i = 1
    cont = 0

    # Estrutura de repeticao
    while i <= num:

        # Estrutura condicional:
        if num % i == 0:
            cont += 1

        # Estrutura condicional: Verificacao 'nao primo'
        if cont > 2:
            break

        # Incremento
        i += 1

    # Estrutura condicional: Primo
    if cont == 2:
        return num

    else:
        return 0

if __name__ == '__main__':
    main()
