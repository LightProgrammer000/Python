'''
Programa: Numeros adjacentes
'''

# Principal
def main():

    # Resultado
    print(num_adj())

# Metodo: Numeros adjacentes
def num_adj():

    # Variaveis
    i = 1
    adj = 0
    n_adj = 0

    # Entrada de dados
    num = int(input("# Digite um número inteiro: "))

    # Estrutura de decisao
    if num < 10:
        return "não"

    else:

        # Estrutura de repeticao
        while i <= num:

            # Algarismo [ultimo]
            alg_ult = ((num // i) % 10)

            # Algarismo [penultimo]
            i *= 10
            alg_pen = ((num // i) % 10)

            # Estrutura de decisao
            if alg_ult == alg_pen:
                adj += 1

            else:
                n_adj += 1

        # Estrutura de decisao
        if adj >= 1:  # Numeros adjacentes repetidos
            return "sim"

        elif n_adj >= 1:  # Numeros adjacentes nao repetidos
            return "não"

# Execucao
if __name__ == '__main__':
    main()
