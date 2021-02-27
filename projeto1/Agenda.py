Agenda = {}


def mostrar_contato():
    if Agenda:
        for contato in Agenda:
            buscar_contato(contato)
            print("------------------------------------------------------------------------------")
    else:
        print("Agenda Vazia!")


def buscar_contato(contato):
    try:
        print("Nome:", contato)
        print("Telefone:", Agenda[contato]["Telefone"])
        print("E-mail: ", Agenda[contato]["E-mail"])
        print("Endereco: ", Agenda[contato]["endereco"])
        print("------------------------------------------------------------------------------")
    except KeyError:
        print("Contato Inexistente")
    except Exception as error:
        print("Um erro inesperado ocorreu!")
        print(error)


def ler_detalhes():
    telefone = input("Insire o Telefone da pessoa: ")
    email = input("Insire o E-mail da pessoa: ")
    endereco = input("Insire o Endereço da pessoa: ")
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    Agenda[contato] = {
        "Telefone": telefone,
        "E-mail": email,
        "endereco": endereco
    }
    salvar()


def excluir_contato(contato):
    try:
        Agenda.pop(contato)
        salvar()
        print(">>>>>>>>>>>>>>>>>>>> {} Excluido dos contatos com sucesso!".format(contato))
    except KeyError:
        print("Contato Inexistente")
    except Exception as error:
        print("Um Erro inesperado ocorreu !")
        print(error)


def exportar_contatos_csv(nome_arquivo):
    try:
        with open(nome_arquivo, "w") as arquivo:
            for contato in Agenda:
                telefone = Agenda[contato]["Telefone"]
                email = Agenda[contato]["E-mail"]
                endereco = Agenda[contato]["endereco"]
                arquivo.write("{}; {}; {}; {}\n".format(contato, telefone, email, endereco))

    except Exception as error:
        print("Algum Erro Ocorreu ao exportar contatos !")
        print(error)


def importar_contatos_csv(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(";")
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print("Arquivo não encontrado! ")
    except Exception as error:
        print("Erro inesperado Ocorreu ao importar contatos! ")
        print(error)


def salvar():
    exportar_contatos_csv("database.csv")


def carregar():
    importar_contatos_csv("database.csv")


def menu():
    print("_______________________________________")
    print("|                                     |")
    print("|         Bem-Vindo a Agenda          |")
    print("|                                     |")
    print("|1 - Mostrar todos contatos da Agenda |")
    print("|2 - Buscar um contato da Agenda      |")
    print("|3 - Incluir um contato na Agenda     |")
    print("|4 - Excluir um contato da Agenda     |")
    print("|5 - Editar um Contato da Agenda      |")
    print("|6 - Exportar Contatos Para CSV       |")
    print("|7 - Importar Contatos de CSV         |")
    print("|0 - Sair do Programa                 |")
    print("|_____________________________________|")

# EXECUÇÃO DO PROGRAMA


carregar()
while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        mostrar_contato()
    elif opcao == "2":
        contato = input("Qual o nome do contato que deseja buscar ? ")
        print("------------------------------------------------------------------------------")
        buscar_contato(contato)
    elif opcao == "3":
        contato = input("Insire o Nome da pessoa: ")
        try:
            Agenda[contato]
            print(">>> Contato ja existente")
        except KeyError:
            telefone, email, endereco = ler_detalhes()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == "4":
        contato = input("Insire o Nome da Pessoa que deseja Excluir da Agenda: ")
        excluir_contato(contato)
    elif opcao == 5:
        contato = input("Insire o Nome da pessoa: ")
        try:
            Agenda[contato]
            print(">>> Editando Contato ....")
            telefone, email, endereco = ler_detalhes()
            incluir_editar_contato(contato, telefone, email, endereco)

        except KeyError:
            print("não é possivel alterar um contato não existente!")
    elif opcao == "6":
        nome_arquivo = input("Digite Nome do Arquivo a ser exportado: ")
        exportar_contatos_csv(nome_arquivo)
        print("Agenda Exportada com sucesso")
    elif opcao == "7":
        nome_arquivo = input("Digite Nome do Arquivo a ser importado: ")
        importar_contatos_csv(nome_arquivo)
    elif opcao == "0":
        break
    else:
        print("Opção Inválida!")
