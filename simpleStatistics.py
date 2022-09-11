'''
- Crie um programa que leia a idade e o sexo de várias pessoas.

- A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar.
No final, mostre:

A - Quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos

'''

# Biblioteca
from emoji import emojize

print(emojize(f"\n\033[0;33m {'=-=' * 15} :mortar_board: DESAFIO :mortar_board: {'=-=' * 15} \033[m\n", use_aliases=True))

# Variáveis: Total
qtd_pes = 0
som_tot_ida = 0
qtd_pes_men18 = 0
qtd_pes_mai18 = 0
lista_ida = []

# Variáveis: Homem
aux_hom1 = 1
qtd_hom = 0
qtd_hom_men20 = 0
qtd_hom_mai20 = 0
soma_ida_hom = 0
lista_ida_hom = []

# Variáveis: Mulher
aux_mul1 = 1
qtd_mul = 0
qtd_mul_men20 = 0
qtd_mul_mai20 = 0
soma_ida_mul = 0
lista_ida_mul = []

# Estrutura de repetição: Menu
while True:

    idade = int(input("\033[0;34m - Digite a idade: \033[m"))

    # Proteção #
    while idade < 0:
        idade = int(input("\033[0;34m - Digite a idade: \033[m"))

    sexo = str(input("\033[0;32m - Digite o sexo [M/F]: \033[m")).upper().strip()

    # Proteção #
    while sexo != 'M' and sexo != 'F':
        sexo = str(input("\033[0;32m - Digite o sexo [M/F]: \033[m")).upper().strip()

    ############################# Homens + Mulheres #############################

    # Controle
    qtd_pes += 1  # Quantidade de pessoas
    som_tot_ida += idade  # Soma total da idades
    lista_ida.append(idade)  # Lista total

    # Idade > 0
    if idade >= 0:

        # Idade < 18
        if idade < 18:
            qtd_pes_men18 += 1

        # Idade > 18
        elif idade >= 18:
            qtd_pes_mai18 += 1

    # Lista: Ordem crescente
    for a in range(0, len(lista_ida)):

        for b in range(0, len(lista_ida) - 1):

            if lista_ida[b] > lista_ida[b + 1]:
                aux = lista_ida[b]
                lista_ida[b] = lista_ida[b + 1]
                lista_ida[b + 1] = aux

    ############################# Homens #############################
    if sexo == 'M':

        # Controle:
        qtd_hom += 1  # Quantidade de homens
        soma_ida_hom += idade  # Soma das idades dos homens
        lista_ida_hom.append(idade)  # Colocar na lista

        # Atribuindo somente 1 vez
        if aux_hom1 == 1:
            maior_ida_hom = idade
            menor_ida_hom = idade
            aux_hom1 = 0

        # Maior idade
        if maior_ida_hom < idade:
            maior_ida_hom = idade

        # Menor idade
        if menor_ida_hom > idade:
            menor_ida_hom = idade

        # Idades entre 20 anos
        if idade >= 0:

            if idade < 20:
                qtd_hom_men20 += 1

            else:
                qtd_hom_mai20 += 1

        # Ordenamento crecente da lista
        for a in range(0, len(lista_ida_hom)):

            for b in range(0, len(lista_ida_hom) - 1):

                if lista_ida_hom[b] > lista_ida_hom[b + 1]:
                    aux_hom2 = lista_ida_hom[b]
                    lista_ida_hom[b] = lista_ida_hom[b + 1]
                    lista_ida_hom[b + 1] = aux_hom2

    ############################# Mulheres #############################
    if sexo == 'F':

        # Controle:
        qtd_mul += 1  # Quantidade das mulheres
        soma_ida_mul += idade  # Soma das idades das mulheres
        lista_ida_mul.append(idade)  # Colocar na lista

        # Atribuindo somente 1 vez
        if aux_mul1 == 1:
            maior_ida_mul = idade
            menor_ida_mul = idade
            aux_mul1 = 0

        # Maior idade
        if maior_ida_mul < idade:
            maior_ida_mul = idade

        # Menor idade
        if menor_ida_mul > idade:
            menor_ida_mul = idade

        # Idades entre 20 anos
        if idade >= 0:

            if idade < 20:
                qtd_mul_men20 += 1

            else:
                qtd_mul_mai20 += 1

        # Ordenamento crecente da lista
        for a in range(0, len(lista_ida_mul)):

            for b in range(0, len(lista_ida_mul) - 1):

                if lista_ida_mul[b] > lista_ida_mul[b + 1]:

                    aux_mul2 = lista_ida_mul[b]
                    lista_ida_mul[b] = lista_ida_mul[b + 1]
                    lista_ida_mul[b + 1] = aux_mul2

    # Menu
    desc = str(input("\n\033[0;31m - Deseja continuar [S/N]: \033[m")).upper().strip()

    # Proteção #
    while desc != 'S' and desc != 'N':
        desc = str(input("\n\033[0;31m - Deseja continuar [S/N]: \033[m")).upper().strip()

    if desc == 'N':
        break

    else:
        print("")

################## RELATÓRIO ##################

#################################### HOMENS + MULHERES ####################################
if qtd_pes != 0:

    # Cálculos
    maior_idade_lista = max(lista_ida)
    menor_idade_lista = min(lista_ida)
    media_total = som_tot_ida / qtd_pes

    print(f"\n\033[0;30m {'=' * 25} RELATÓRIO {'=' * 25} \033[m")
    print(f"\033[0;31m - Pessoas cadastradas: {qtd_pes} \033[m")
    print(f"\033[0;32m - Pessoas com mais de 18 anos: {qtd_pes_mai18} \033[m")
    print(f"\033[0;33m - Pessoas com menos de 18 anos: {qtd_pes_men18} \033[m")
    print(f"\033[0;34m - Maior idade: {maior_idade_lista} \033[m")
    print(f"\033[0;35m - Menor idade: {menor_idade_lista} \033[m")
    print(f"\033[0;36m - Média de idade: {media_total:.2f} \033[m")

    print(" Lista das idades: ", end="")
    for i in range(0, len(lista_ida)):
        print(f"\033[0;36m {lista_ida[i]}", end="\033[0;30m -> \033[m")
    print("Acabou")

    print(f"\033[0;30m {'=' * 61} \033[m")

#################################### HOMENS ####################################

if qtd_hom != 0:

    # Cálculos
    med_ida_hom = soma_ida_hom / qtd_hom

    print(f"\n\033[0;30m {'=' * 25} RELATÓRIO {'=' * 25} \033[m")
    print(f"\033[0;31m - Homens cadastrados: {qtd_hom} \033[m")
    print(f"\033[0;32m - Homens com menos de 20 anos: {qtd_hom_men20} \033[m")
    print(f"\033[0;33m - Homens com mais de 20 anos: {qtd_hom_mai20} \033[m")
    print(f"\033[0;34m - Maior idade: {maior_ida_hom} \033[m")
    print(f"\033[0;35m - Menor idade: {menor_ida_hom} \033[m")
    print(f"\033[0;36m - Média de idade: {med_ida_hom:.2f} \033[m")

    print(" Lista das idades dos homens: ", end="")
    for i in range(0, len(lista_ida_hom)):
        print(f"\033[0;36m {lista_ida_hom[i]}", end="\033[0;30m -> \033[m")
    print("Acabou")

    print(f"\033[0;30m {'=' * 61} \033[m")

#################################### MULHERES ####################################

if qtd_mul != 0:

    # Cálculos
    med_ida_mul = soma_ida_mul / qtd_mul

    print(f"\n\033[0;30m {'=' * 25} RELATÓRIO {'=' * 25} \033[m")
    print(f"\033[0;31m Mulheres cadastradas: {qtd_mul} \033[m")
    print(f"\033[0;32m - Mulheres com menos de 20 anos: {qtd_mul_men20} \033[m")
    print(f"\033[0;33m - Mulheres com mais de 20 anos: {qtd_mul_mai20} \033[m")
    print(f"\033[0;34m - Maior idade: {maior_ida_mul} \033[m")
    print(f"\033[0;35m - Menor idade: {menor_ida_mul} \033[m")
    print(f"\033[0;36m - Média de idade: {med_ida_mul:.2f} \033[m")

    print(" Lista das idades das mulheres: ", end="")
    for i in range(0, len(lista_ida_mul)):
        print(f"\033[0;36m {lista_ida_mul[i]}", end="\033[0;30m -> \033[m")
    print("Acabou")
    print(f"\033[0;30m {'=' * 61} \033[m")

'''
- CORES NO TERMINAL
Ex.: \033[ESTILO;TEXTO;FUNDOm <TEXTO> \033[m

STYLE                    TEXT                   BACKGROUND                 
0 - None                 30 - Branco            40 - Branco
1 - Bold                 31 - Vermelho          41 - Vermelho
4 - Underline            32 - Verde             42 - Verde
7 - Negative (Inversão)  33 - Amarelo           43 - Amarelo
                         34 - Azul              44 - Azul
                         35 - Roxo              45 - Roxo
                         36 - Azul Piscina      46 - Azul Piscina
                         37 - Cinza (Padrão)    47 - Cinza (Padrão)
'''
