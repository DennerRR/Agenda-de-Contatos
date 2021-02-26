

Agenda = {
    "João ":{
        "tel": "99999-1001",
        "E-mail":"ContatoJoao@solyd.com.br",
        "endereco" : "Rua sebatião juventus"
    },
    "Maria ":{
        "tel": "222229-1001",
        "E-mail":"ContatoMaria@solyd.com.br",
        "endereco" : "avenida 2"
    },
    "Pedro ":{
        "tel": "33333-33333",
        "E-mail":"ContatoPedro@solyd.com.br",
        "endereco" : "Avenida3"
    },
    "Rogerio":{
        "tel": "444444-44444",
        "E-mail":"ContatoRogerio@solyd.com.br",
        "endereco" : "Avenida 4"
    }
}
def mostrarContato():
    for contato in Agenda:
        print("Nome:", contato)
        print("Telefone:", Agenda[contato]['tel'])
        print("E-mail: ", Agenda[contato]['E-mail'])
        print("Endereco: ", Agenda[contato]['endereco'])
        print("------------------------------------------------------------------------------")

mostrarContato()