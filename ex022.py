nome = str(input("Insira o nome de uma pessoa: ")).strip()

print("O nome com todas as letras maiúsculas: {}".format(nome.upper()))
print("O nome com todas as letras minúsculas: {}".format(nome.lower()))

print("Quantas letras ao todo (Sem espaços): {}".format(len(nome) - nome.count(" ")))

print("Quantas letras tem o primeiro nome: {}".format(len(nome.split()[0])))
