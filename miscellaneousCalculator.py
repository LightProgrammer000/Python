"""
Python: 3
Program: Calculadora
"""

# Importacoes
from os import system
from emoji import emojize

#######################
# METODOS MATEMATICOS #
#######################
def Somatorio():

    system("clear")
    print("\n\033[01;32m=== Somatorio ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;33m# Digite N1: \033[01;37m"))
    n2 = int(input("\033[01;34m# Digite N2: \033[01;37m"))

    # Calculo e impressao
    print("\033[01;35m# Resultado: {} \033[01;37m".format(n1 + n2))

def Subtracao():

    system("clear")
    print("\n\033[01;32m=== Subtracao ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;33m# Digite N1: \033[01;37m"))
    n2 = int(input("\033[01;34m# Digite N2: \033[01;37m"))

    # Calculo e impressao
    print("\033[01;35m# Resultado: {} \033[01;37m".format(n1 - n2))

def Multiplicacao():

    system("clear")
    print("\n\033[01;32m=== Multiplicacao ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;33m# Digite N1: \033[01;37m"))
    n2 = int(input("\033[01;34m# Digite N2: \033[01;37m"))

    # Calculo e impressao
    print("\033[01;35m# Resultado: {} \033[01;37m".format(n1 * n2))

def Divisao():

    system("clear")
    print("\n\033[01;32m=== Divisao ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;33m# Digite N1: \033[01;37m"))
    n2 = int(input("\033[01;34m# Digite N2: \033[01;37m"))

    # Estrutura de Loop: Protecao contra divisao por "0"
    while n2 == 0:
        print("\n\033[01;31m* Divisao por ZERO nao pode, pois resulta em infinito \033[01;37m")
        n2 = int(input("\033[0;33m# {} \033[01;37m".format("Digite N2: ")))

    # Calculo e impressao
    print("\n\033[01;35m# Resultado ({}): {:.2f} \033[01;37m".format(str(n1) + "/" + str(n2), n1 / n2))

def VerificaPrimo():

    # Variaveis locais
    resto = 0

    system("clear")
    print("\n\033[01;32m=== Identificando numeros primos ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;33m# {} \033[01;37m".format("Digite N1:")))

    # Estrutura de condicao: Protecao contra numeros negativos
    if n1 <= 0:
        print("\n\033[01;31m# {} \033[01;37m\n".format("Numero Invalido"))

    # Estrutura de decisao: Protecao contra o numero "1"
    elif n1 == 1:
        print("\n\033[01;32m# {} \033[01;37m\n".format("Divisor universal"))

    else:
        # Estrutura condicional: Resto da divisao igual a "0"
        # Ex: numero = 89 --> Sera dividido por (1 ate (88+1))
        for contador in range(1, (n1 + 1)):
            if n1 % contador == 0:
                resto += 1  # Acrescenta "1" a variavel resto

            # Caso a quantidade de restos iguais a "0" for maior que 2, nao e primo
            if resto > 2:
                print("\033[01;31m# {} \033[0;37m".format("Resultado: Nao Primo"))
                break

        # Numeros primos sao sempre divididos por "1" e por ele mesmo, logo terao "2" restos iguais a "0"
        if resto == 2:
            print("\033[01;32m# {} \033[01;37m".format("Resultado: Primo"))

def Potenciacao():

    system("clear")
    print("\n\033[01;32m=== Potenciacao ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;33m# {} \033[01;37m".format("Digite a base: ")))
    n2 = int(input("\033[01;34m# {} \033[01;37m".format("Digite o expoente: ")))

    # Calculo e impressao
    print("\033[01;32m# Resultado: {} \033[01;37m".format(str(n1 ** n2)))

def Radiciacao():

    system("clear")
    print("\n\033[01;32m=== Radiciacao ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;33m# {} \033[01;37m".format("Digite o numero: ")))
    n2 = int(input("\033[01;34m# {} \033[01;37m".format("Digite a raiz: ")))

    # Calculo e Impressao (manobra matematica de inverter o numero antes para depois o elevar, extraindo a sua raiz)
    print("\033[01;32m# Resultado: {} \033[01;37m".format(str(n1 ** (n2 ** (-1)))))

def Porcentagem():

    system("clear")
    print("\n\033[01;32m=== PORCENTAGEM ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;33m# {} \033[01;37m".format("Digite o percentual (Sem o sinal %): ")))
    n2 = int(input("\033[01;34m# {} \033[01;37m".format("Digite um valor: ")))

    # Calculo e Impressao
    print("\033[01;32m# Resultado: {} % de {} = {}\033[01;37m".format(n1, n2, 0.01 * n1 * n2))

def Divisores():

    system("clear")
    print("\n\033[01;32m=== Divisores ===\033[01;37m\n")

    # Entrada de variaveis
    n1 = int(input("\033[01;34m# {} \033[01;37m".format("Digite um valor: ")))

    # Calculo e Impressao
    print("\n\033[01;32m# {} \033[01;37m".format("Resultados: "))

    for divisores in range(1, (n1 + 1)):

        if n1 % divisores == 0:
            print("\033[01;32m# {} \033[01;37m".format(divisores))

def Fatorial():

    system("clear")
    print("\n\033[01;32m=== Fatorial ===\033[01;37m\n")

    fat = int(input("\033[01;34m# {} \033[01;37m".format("Digite um valor: ")))

    if fat == 0:
        print("\033[01;32m# {} \033[01;37m".format("Resultado: 1 "))

    else:
        for contador in range(1, fat):

            # fat = fat * contador (Ex: fat = fat * 1)
            fat *= contador
        print("\033[01;32m# {} {} \033[01;37m".format("Resultado:", fat))

#######################
# METODOS DE CONTROLE #
#######################
def decisoes(opcao):

    # SAIDA
    if opcao == "0":
        return False

    # SOMATORIO
    elif opcao == "1":
        Somatorio()

    # SUBTRACAO
    elif opcao == "2":
        Subtracao()

    # MULTIPLICACAO
    elif opcao == "3":
        Multiplicacao()

    # DIVISAO
    elif opcao == "4":
        Divisao()

    # VERIFICADOR DE NUMERO PRIMO
    elif opcao == "5":
        VerificaPrimo()

    # POTENCIACAO
    elif opcao == "6":
        Potenciacao()

    # RADICIACAO
    elif opcao == "7":
        Radiciacao()

    # PORCENTAGEM
    elif opcao == "8":
        Porcentagem()

    # DIVISORES
    elif opcao == "9":
        Divisores()

    # FATORIAL
    elif opcao == "10":
        Fatorial()

    # Retorno Verdadeiro para quaisquer opcoes (Retornando ao Menu)
    input("\n<< PRESS ENTER >>")
    return True

# MENU
def menu():

    system("clear")
    print(emojize("\n\033[01;32m {1} {0} MATEMATICA {0} {1}\033[01;37m".format(":computer:", "=-=" * 10),
                  use_aliases=True))

    # Lista de Menu
    a = 0
    listaMenu = {"sai": "Sair",
                 "som": "Soma",
                 "sub": "Subtracao",
                 "mul": "Multiplicacao",
                 "div": "Divisao",
                 "pri": "Verificador de numero primo",
                 "pot": "Potenciacao",
                 "rad": "Radiciacao",
                 "por": "Porcentagem",
                 "divs": "Divisores",
                 "fat": "Fatorial",
                 }

    for i in listaMenu:

        print("\033[01;3{}m {}) {} \033[01;37m".format(a, a, listaMenu[i]))
        a += 1
    print("\n\033[01;32m {}\033[01;37m".format("=-=" * 27))

    # Escolha do menu
    return decisoes(input("\033[01;31m {} \033[01;37m".format("# Opcao: ")))

# Programa principal
def main():

    # Variavel de controle
    ctrl = True

    try:
        while ctrl:
            ctrl = menu()

    except Exception as e:
        # print(e)
        pass
if __name__ == '__main__':
    main()
