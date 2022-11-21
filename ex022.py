nome = input("Insira um nome completo: ")

print("O nome da pessoa com todas as letras maiúsculas: {}".format(nome.upper()))
print("O nome co todas as letras minúsculas: {}".format(nome.lower()))

contletras = len(nome) - nome.count(" ")
print("Quantas letras ao todo: {}".format(contletras))

print("O primeiro nome tem {} letras".format(len(nome.split()[0])))
