
Agenda = {
    "Joao": {
        "Telefone": "99999-1001",
        "E-mail": "ContatoJoao@solyd.com.br",
        "endereco": "Rua sebastiao juventus"
    },
    "Maria": {
        "Telefone": "222229-1001",
        "E-mail": "ContatoMaria@solyd.com.br",
        "endereco": "avenida 2"
    },
    "Pedro": {
        "Telefone": "33333-33333",
        "E-mail": "ContatoPedro@solyd.com.br",
        "endereco": "Avenida3"
    },
}


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


def incluir_editar_contato(contato):
    telefone = input("Insire o Telefone da pessoa: ")
    email = input("Insire o E-mail da pessoa: ")
    endereco = input("Insire o Endereço da pessoa: ")

    Agenda[contato] = {
        "Telefone": telefone,
        "E-mail": email,
        "endereco": endereco
    }


def excluir_contato(contato):
    try:
        Agenda.pop(contato)
        print(">>>>>>>>>>>>>>>>>>>> {} Excluido dos contatos com sucesso!".format(contato))
    except KeyError:
        print("Contato Inexistente")
    except Exception as error:
        print("Um Erro inesperado ocorreu !")
        print(error)


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
    print("|0 - Sair do Programa                 |")
    print("|_____________________________________|")


while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        mostrar_contato()
    elif opcao =="2":
        contato = input("Qual o nome do contato que deseja buscar ? ")
        print("------------------------------------------------------------------------------")
        buscar_contato(contato)
    elif opcao == "3" :
        contato = input("Insire o Nome da pessoa: ")
        try:
            Agenda[contato]
            print(">>> Contato ja existente")
        except KeyError:
            incluir_editar_contato(contato)
    elif opcao == 5:
        contato = input("Insire o Nome da pessoa: ")
        try:
            Agenda[contato]
            print(">>> Editando Contato ....")

            incluir_editar_contato(contato)
        except KeyError:
            print("não é possivel alterar um contato não existente!")
    elif opcao == "4":
        contato = input("Insire o Nome da Pessoa que deseja Excluir da Agenda: ")
        excluir_contato(contato)
    elif opcao == "0":
        break
    else:
        print("Opção Inválida!")



