def main():
    print("\n {0} MEDIA {0}".format("=-=" * 5, "=-=" * 5))

    # Entrada de dados
    nota_1 = float(input(" - Nota 1: "))
    nota_2 = float(input(" - Nota 2: "))

    media(nota_1, nota_2)

    if 0 < media(nota_1, nota_2) < 5.00:
        print(situacao(media(nota_1, nota_2)))

    elif 5.00 <= media(nota_1, nota_2) <= 10:
        print(situacao(media(nota_1, nota_2)))

    else:
        print(situacao(media(nota_1, nota_2)))

# Funcao: Media
def media(a, b):
    return (a + b) / 2

# Funcao: Situacao
def situacao(a):
    if 0 < a < 5.00:
        return "\n - Situacao: Reprovado"

    elif 5.00 <= a <= 10:
        return "\n - Situacao: Aprovado"

    else:
        return "\n - Situacao: Recuperacao"

# Chamada de funcao principal
main()
