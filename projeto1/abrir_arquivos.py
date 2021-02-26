try:
    arquivo = open("emails.txt")
    print(arquivo.read())
except FileNotFoundError as e:
    print("Arquivo não encontrado! ")
    print(e)
finally:
    #Caso o arquivo não exista ira ocorrer um erro ao fechar um arquivo inexistente
    arquivo.close()
    # Jeito melhor
try:
    with open("emails.txt") as arquivo:
        print(arquivo.readlines())
except FileNotFoundError:
    print("Arquivo não Encontrado! ")
except:
    print("Um Erro Inesperado ocorreu! ")
