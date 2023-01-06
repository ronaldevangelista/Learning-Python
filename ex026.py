frase = str(input("Insira aqui a sua frase: ")).strip().lower()

print("A letra aparece {} vezes".format(frase.count("a")))
print("A primeira posição da letra a é: {0} (ou {1}º)".format(frase.find("a"), frase.find("a") + 1))
print("A última posição da letra a é: {0} (ou {1})º".format(frase.rfind("a"), (frase.rfind("a") + 1)))
