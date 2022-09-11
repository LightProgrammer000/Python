import os

# Variaveis
a = 0
acumulador = 0
limite = 50 * pow(10, 6)

while True:

    os.system("cls")
    print("\033[01;34m ------------------------------------- \033[01;37m")
    print("\033[01;35m -------- ORCAMENTO TEMPO REAL ------- \033[01;37m")
    print("\033[01;34m ------------------------------------- \033[01;37m")
    print("")
    print("\033[01;32m # Caixa : " + str(float(limite - a)) + "\033[01;37m")
    print("\033[01;31m # Despesas : " + str(float(acumulador)) + "\033[01;37m")

    # Entrada de dados
    a = float(input("\033[01;36m\n * Digite o valor: \033[01;37m"))
    acumulador += a

    if a > limite:
        print("\033[01;33m\n => Nao tem dinheiro \n\033[01;36m")
        break

    elif acumulador <= limite:
        continue

    elif acumulador > limite:
        print("\033[01;33m\n => Nao tem dinheiro \n\033[01;36m")
        break
