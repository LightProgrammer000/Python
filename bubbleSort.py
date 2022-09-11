'''
Programa: Bubble sort
'''

# Principal
def main():

    lista = [1, 2, 3]

    print(buuble_sort(lista))

# Metodo: Maior elemento
def buuble_sort(lista):

    i = 1
    aux = 0

    # Estrutura de repeticao
    while i < len(lista):

        # Reiniciando variavel
        j = 0

        # Estrutura de repeticao
        while j <= i:

            # Estrutura de decisao
            if lista[i] > lista[j]:

                # Troca de valores
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

            # Incremento
            j += 1

        # Incremento
        i += 1

    return lista

# Execucao
if __name__ == '__main__':
    main()
