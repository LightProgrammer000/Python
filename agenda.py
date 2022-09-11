"""
Python: 3
Project: Agenda interativa
Estrutura de dados: Dicionario

* Observacoes
Obs(1): Comentar todas as linhas de uma vez ⇨ ctrl + /
Obs(2): Forma de declaracao alternativa: AGENDA = dict()
Obs(3): Lista = []
Obs(4): Tupla = ()
Obs(5): Conjunto = {}
"""

# Importacoes
from os import system

##############
# DICIONARIO #
##############

# Forma de declaracao comum
AGENDA = {}

###########
# METODOS #
###########

# Mostrar contatos da agenda
def mostrarContatos():
    print("{}".format("\n\033[01;32m### CONTATOS ### \033[01;37m"))

    # Estrutura de decisao: Analisar quantidade de contatos da agenda
    if len(AGENDA) > 0:

        # i -> Contato
        for i in AGENDA:
            print("\n# {}: {}".format("ID", i))

            # j -> [telefone] [email] [endereco]
            for j in AGENDA[i]:
                print("# {}: {}".format(j, AGENDA[i][j]))
    else:
        print("{}".format("\033[01;32m# Agenda nao possui contatos\033[01;37m"))

    print("{}".format("\033[01;32m###\033[01;37m" * 15))

# Buscando contatos especificos
def buscarContatos(nome):

    try:
        print("\n# {} {}".format("ID: ", nome))

        for i in AGENDA[nome]:
            print("# {}: {}".format(i, AGENDA[nome][i]))

        print("{}".format("\033[01;32m#\033[01;37m" * 45))

    except KeyError:
        print("{}".format("\033[01;31m# Contato invalido\033[01;37m"))

# Incluindo contatos
def incluirEditarContato(contato, telefone, email, endereco):

    # Adicionando ao dicionario no estilo Hard Code
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }

    # Metodo: Salvar no arquivo database.csv
    save()
    print("\n\033[01;36m# Contato '{}' adicionado/editado com sucesso \033[01;37m".format(contato))

# Excluir contato
def excluirContato(contato):

    try:
        AGENDA.pop(contato)
        print("\n\033[01;31m# Contato '{}' excluido com sucesso \033[01;37m".format(contato))

        # Metodo: Salvar no arquivo database.csv
        save()

    except KeyError as e:
        print("{}".format("\033[01;31m# Contato invalido\033[01;37m"))

# Exportando contatos em TXT
def exportarContatosTXT():

    try:
        # w: Reescrever os contatos na agenda
        with open("agenda.txt", "w") as arquivo:

            for i in AGENDA:
                arquivo.write("\n\n{}: {}".format("# Contato", i))

                for j in AGENDA[i]:
                    arquivo.write("\n{}: {}".format(j, AGENDA[i][j]))

        print("{}".format("\033[01;32m# Agenda exportada com sucesso\033[01;37m"))

    except Exception as e:
        print("{}".format("\033[01;31m# Exportacao invalida\033[01;37m"))

# Exportando contatos em CSV
def exportarContatosCSV():

    try:
        with open("exportar.csv", "w") as arquivo:

            for i in AGENDA:
                arquivo.write("\n{}".format(i))

                for j in AGENDA[i]:
                    arquivo.write(",{}".format(AGENDA[i][j]))

        # Shell Script
        system("cat exportar.csv | grep -i ' ' > tmp.csv;"
               "rm -rf exportar.csv;"
               "mv tmp.csv exportar.csv")

    except Exception as e:
        print("{}".format("\033[01;31m# Exportacao invalida\033[01;37m"))

# Exportando contatos em CSV
def exportarDatabase():

    try:
        with open("database.csv", "w") as arquivo:

            for i in AGENDA:
                arquivo.write("\n{}".format(i))

                for j in AGENDA[i]:
                    arquivo.write(",{}".format(AGENDA[i][j]))

        # Shell Script
        system("cat database.csv | grep -i ' ' > tmp.csv;"
               "rm -rf database.csv;"
               "mv tmp.csv database.csv")

    except Exception as e:
        print("{}".format("\033[01;31m# Exportacao invalida\033[01;37m"))

    """
    # Codigo Alternativo
    try:
        # w: Reescrever os contatos na agenda
        with open(exportar + ".csv", "w") as arquivo:

            for i in AGENDA:
                arquivo.write("{},{},{},{}\n".format(i, AGENDA[i]["telefone"], AGENDA[i]["email"], AGENDA[i]["endereco"]))

        print("{}".format("\033[01;32m# Agenda exportada com sucesso\033[01;37m"))

    except Exception as e:
        print("{}".format("\033[01;31m# Exportacao invalida\033[01;37m"))
    """

# Importar contatos avulsos
def importarContatos(importar):

    try:
        with open(importar + ".csv", "r") as arq:

            # Estrutura de repeticao: Leitura de linhas de uma arquivo em lista
            for i in arq.readlines():

                # Transformacao em lista com delimitador de ","
                info = i.strip().split(",")

                # Chamada de metodo para importar contato
                incluirEditarContato(info[0], info[1], info[2], info[3])

    except Exception as e:
        print("{}".format("\033[01;31m# Importacao invalida\033[01;37m"))

###################
# METODOS SUPORTE #
###################

# Entrada de dados em detalhes sobre o contato
def entradaDadosContato():

    print("")
    telefone = input("{}".format("\033[01;34m# Telefone: \033[01;37m"))
    email = input("{}".format("\033[01;34m# Email: \033[01;37m"))
    endereco = input("{}".format("\033[01;34m# Endereco: \033[01;37m"))

    return telefone, email, endereco

# Carregar o banco de dados 'database.csv'
def load():

    try:
        with open("database.csv", "r") as arq:

            # Estrutura de repeticao: Leitura de linhas de uma arquivo em lista
            for i in arq.readlines():

                # Transformacao em lista com delimitador de ","
                info = i.strip().split(",")

                # Incluindo no Dicionario
                AGENDA[info[0]] = {
                    "telefone": info[1],
                    "email": info[2],
                    "endereco": info[3]
                }

        # Mensagem de confirmacao
        print("{} {} contatos".format("Database adicionado com sucesso", len(AGENDA)))

    except Exception as e:
        print("Erro inesperado")
        print(e)

# Salvar estado atual da agenda no arquivo 'database.csv'
def save():
    exportarDatabase()
    pass

################################
# METODOS DE CONTROLE DE FLUXO #
################################

# Menu interativo
def menu():
    system("clear")
    print("{}".format("\033[01;31m### MENU ###\033[01;37m"))
    print("{}".format("=" * 50))
    print("{}".format("\033[01;32m[1] Mostrar contatos da agenda\033[01;37m"))
    print("{}".format("\033[01;33m[2] Buscar contato\033[01;37m"))
    print("{}".format("\033[01;34m[3] Incluir contato\033[01;37m"))
    print("{}".format("\033[01;35m[4] Editar contato\033[01;37m"))
    print("{}".format("\033[01;36m[5] Excluir contato\033[01;37m"))
    print("{}".format("\033[01;37m[6] Exportar contatos em arquivo [txt]\033[01;37m"))
    print("{}".format("\033[01;31m[7] Exportar contatos em arquivo [csv]\033[01;37m"))
    print("{}".format("\033[01;32m[8] Importar contatos em arquivo [csv]\033[01;37m"))
    print("{}".format("\033[01;33m[0] Saida\033[01;37m"))
    print("{}".format("=" * 50))

    # Entrada de opcoes
    opc = input("{}".format("\033[01;34m# Opc.: \033[01;37m"))
    system("clear")

    # Estruturas de decisoes: Opcoes de MENU
    if opc == "0":
        exit(1)

    # Mostrar contatos da agenda
    elif opc == "1":
        mostrarContatos()

    # Buscar contato
    elif opc == "2":
        print("\n{}".format("\033[01;32m### BUSCANDO ###\033[01;37m"))
        buscarContatos(input("\n{}".format("\033[01;34m# Contato: \033[01;37m")))

    # Incluir contato
    elif opc == "3":
        print("\n{}".format("\033[01;32m### Incluir Contato ###\033[01;37m"))
        contato = input("\n{}".format("\033[01;34m# Contato: \033[01;37m"))

        try:
            if AGENDA[contato]:
                print("\033[01;34m{}\033[01;37m".format("# Contato existente"))

        except KeyError:
            print("\033[01;35m{}\033[01;37m".format("# Incluir dados do novo contato"))

            # Metodo: Inclusao dos detalhes do contato
            telefone, email, endereco = entradaDadosContato()
            incluirEditarContato(contato, telefone, email, endereco)

    # Editar contato
    elif opc == "4":
        print("\n{}".format("\033[01;32m### Editando Contato ###\033[01;37m"))
        contato = input("\n{}".format("\033[01;34m# Contato: \033[01;37m"))

        try:
            if AGENDA[contato]:
                print("\033[01;34m{}\033[01;37m".format("# Editando dados do contato"))

                # Metodo: Edicao dos detalhes do contato
                telefone, email, endereco = entradaDadosContato()
                incluirEditarContato(contato, telefone, email, endereco)

        except KeyError:
            print("\033[01;34m{}\033[01;37m".format("# Contato inexistente"))

    # Excluir contato
    elif opc == "5":
        print("\n{}".format("\033[01;32m### Excluindo Contato ###\033[01;37m"))
        excluirContato(input("\n{}".format("\033[01;34m# Contato: \033[01;37m")))

    # Exportando contatos em arquivo TXT
    elif opc == "6":
        print("\n{}".format("\033[01;32m### Exportando Contato ###\033[01;37m"))
        exportarContatosTXT()

    # Exportando contatos em arquivo CSV
    elif opc == "7":
        print("\n{}".format("\033[01;32m### Exportando Contato ###\033[01;37m"))
        exportarContatosCSV()

    # Importando contatos em arquivo CSV
    elif opc == "8":
        print("\n{}".format("\033[01;32m### Importando Contatos ###\033[01;37m"))
        importarContatos(input("{}".format("# Nome do arquivo: ")))

    # Pause de retorno de menu
    input("\n{}".format("\033[01;36m<< Press Enter >>\033[01;37m"))

# Metodo principal
def main():

    # Carregar contatos
    load()
    while True:
        try:
            menu()

        except Exception as e:
            print("{}".format("\033[01;31m Erro inesperado \033[01;37m"))

        finally:
            pass

# Inicializacao do programa
if __name__ == '__main__':
    main()
