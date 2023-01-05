frase = input("Insira aqui a sua frase: ")

print("A letra aparece {} vezes".format(frase.lower().count("a")))
print("A primeira posição da letra a é: {} (ou {}º)".format(frase.lower().find("a"), frase.lower().find("a") + 1))
#print("A última posição da letra é: {} (ou {1}º".format(frase.find("a") + 1, frase.find()))