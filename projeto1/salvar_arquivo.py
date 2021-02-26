try:
    with open("nomes.txt", "a") as arquivo:
        arquivo.write("Denner\n")
        arquivo.write("Joao\n")
        arquivo.write("Maria\n")
except Exception as error:
    print("Algum Erro Ocorreu!")
    print(error)