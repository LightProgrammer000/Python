'''
Programa: Invertendo sequência
'''

# Principal
def main():

    # Variavel
    ctrl = True
    lista = []

    # Estrutura de repeticao
    while ctrl:

        # Chamada de metodo
        a = ent_dad()

        # Estrutura de decisao
        if a == 0:
            ctrl = False

        else:

            # Incluir na lista
            lista.append(a)

    # Estrutura de repeticao
    print("")
    for i in range((len(lista) - 1), -1, -1):
        print(lista[i])

# Metodo: Maior elemento
def ent_dad():

    # Entrada de dados
    num = int(input("Digite um número:"))

    return num

# Execucao
if __name__ == '__main__':
    main()
