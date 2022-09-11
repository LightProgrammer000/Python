'''
Programa: Numero primo
'''

# Principal
def main():

    # Funcao
    return maior_primo(10)

# Metodo: Maior primo
def maior_primo(n):

    # Variaveis
    maior = 0

    # Estrutura de decisao: Abaixo de '0'
    if n <= 0:
        print("Invalido")
        exit(0)

    # Estrutura de decisao: 1
    elif n == 1:
        print("Divisor universal")
        exit(0)

    else:

        # Estrutura de repeticao: Numero acima de '0'
        while n > 0:

            # Apresentacao
            a = int(primo(n))
            # print(a)

            # Estrutura de decisao: Verificao do maior primo
            if a >= maior:
                maior = a

            # Decremento
            n -= 1

    return maior

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

# Execucao
if __name__ == '__main__':
    print(main())
