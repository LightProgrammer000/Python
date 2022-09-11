# Programa: EX_06

# Importacao
import math

# Mensagem
print("\n {0} Equacao do 2º grau {0} ".format(3 * "=-=", 3 * "=-="))
print(" - Equacao geral: ax² + bx + c")

# Entrada de dados
a = float(input(" - Digite a: "))
b = float(input(" - Digite b: "))
c = float(input(" - Digite c: "))

# Equacao do 2º grau
delta = b**2 - 4 * a * c

# Estrutura de decisao
if delta > 0:
    print("\n ### Existem duas raizes reais ###")

    # Raiz 1
    raiz_1 = (b + math.sqrt(delta)) / 2 * a

    # Raiz 2
    raiz_2 = (-b + math.sqrt(delta)) / 2 * a

    # Mensagem
    print(" - Raiz 1: {0}".format(raiz_1))
    print(" - Raiz 2: {0}".format(raiz_2))

elif delta == 0:

    print("\n ### Existe 1 raiz real ###")

    # Raiz
    raiz = (-b / 2 * a)

    # Mensagem
    print(" - Raiz: {0}".format(raiz))

else:
    print("\n - 2 raizes nao reais")
