'''
- Crie um programa que simule o funcionamento de um caixa eletrônico

- No início, pergunte ao usuário qual será o valor a ser sacado
(Número Inteiro)

- Informar quantas cédulas de cada valor serão entregues.

Obs.:
Considere que o caixa possui cédulas:
- R$ 50
- R$ 20
- R$ 10
- R$ 1

'''
# Biblioteca
from emoji import emojize

# Variáveis
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_01 = 0

print(emojize(f"\n\033[0;33m {'=-=' * 15} :mortar_board: DESAFIO 71 :mortar_board: {'=-=' * 15} \033[m\n", use_aliases=True))

n = int(input("\033[0;34m Digite um valor: \033[m"))

while n > 0:

    # Notas: R$ 50,00
    while n >= 50:

        # Resto: Igual ou menor 50
        if n % 50 <= 50:
            nota_50 += 1
            n -= 50

    # Notas: R$ 20,00
    while n >= 20:

        # Resto: Igual ou menor 20
        if n % 20 <= 20:
            nota_20 += 1
            n -= 20

    # Notas: R$ 10,00
    while n >= 10:

        # Resto: Igual ou menor 10
        if n % 10 <= 10:
            nota_10 += 1
            n -= 10

    # Notas: R$ 1,00
    while n >= 1:

        # Resto: Igual ou menor 1
        if n % 1 <= 1:
            nota_01 += 1
            n -= 1

print(f"\n\033[0;30m {'=' * 25} BANCO CENTRAL {'=' * 25} \033[m")
print(f"\033[0;31m - Número de Notas R$ 50,00: {nota_50} \033[m")
print(f"\033[0;32m - Número de Notas R$ 20,00: {nota_20} \033[m")
print(f"\033[0;33m - Número de Notas R$ 20,00: {nota_10} \033[m")
print(f"\033[0;34m - Número de Notas R$  1,00: {nota_01} \033[m")
print(f"\033[0;30m {'=' * 65} \033[m")
