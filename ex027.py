nm = input("Insira o nome completo de uma pessoa: " )
split = nm.split()
lenght = len(split) - 1
print("Primeiro: {}".format(split[0]))
print("Último: {}".format(split[lenght]))
