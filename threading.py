# Biblioteca
from time import sleep
from threading import Thread

# Funcao: Carrinho 1
def carrinho_1(velocidade, tempo):

    # Variaveis
    distancia = 0

    # Estrutura de repeticao
    while distancia <= 300:

        # Mensagem
        print(" # Carrinho 1 [distancia]: ", str(distancia))

        # Incremento
        distancia += velocidade * tempo
        sleep(2.0)

    print("\033[01;34m\n - Carrinho 1 chegou \033[01;37m")

# Funcao: Carrinho 1
def carrinho_2(velocidade, tempo):

    # Variaveis
    distancia = 0

    # Estrutura de repeticao
    while distancia <= 300:

        # Mensagem
        print(" # Carrinho 2 [distancia]: ", str(distancia))
        print("")

        # Incremento
        distancia += velocidade * tempo
        sleep(2.0)

    print("\033[01;34m\n - Carrinho 2 chegou \033[01;37m")

# Principal
def main():

    # Threads
    thread_Carrinho1 = Thread(target=carrinho_1, args=[10, 3])
    thread_Carrinho2 = Thread(target=carrinho_2, args=[10, 4])

    # Start
    thread_Carrinho1.start()
    thread_Carrinho2.start()

# Execucao
if __name__ == '__main__':
    main()
