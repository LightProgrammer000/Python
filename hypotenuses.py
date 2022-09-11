'''
Programa: Soma de hipotenusas
'''

# Principal
def main():

    # Resultado
    print(soma_hipotenusas(25))

# Metoo: Hipotenusa
def e_hipotenusa(hip, i, j):

    # Calculos: Hipotenusa
    verf_1 = int(hip ** 2 == i ** 2 + j ** 2)

    # Verificando existencia do triangulo
    a = abs(i - j) < hip < i + j
    b = abs(hip - j) < i < hip + j
    c = abs(hip - i) < j < hip + i
    verf_2 = a and b and c

    # Estrutura de decisao
    if verf_1 and verf_2:
        return hip

    else:
        return 0

# Metodo: Somatorio
def soma_hipotenusas(n):

    # n² = i² + j²
    hip = 1
    soma = 0
    aux = 0  # Controle para bloquear numeros repetidos

    # Estruturas de repeticao
    while hip <= n:

        # # Variavel reiniciada
        i = 1

        # Estrutura de repeticao: Cateto <= Hipotenusa
        while i <= hip:

            # Variavel reiniciada
            j = 1

            # Estrutura de repeticao: Cateto menor <= Cateto maior
            while j <= i:

                # Chamada de metodo
                a = e_hipotenusa(hip, i, j)

                # Estrutura de decisao: Controle de repeticao de numeros
                if a != 0 and a != aux:

                    # print(a)
                    soma += a
                    aux = a

                # Incrementador do cateto menor
                j += 1

            # Incrementador do cateto maior
            i += 1

        # Incrementador da hipotenusa
        hip += 1

    return soma

# Execucao
if __name__ == '__main__':
    main()
