cidade = str(input("Digite o nome de uma cidade brasileira: "))

print("Essa cidade começa com 'Santo'? {}".format("santo" in cidade.lower().split()[0]))
