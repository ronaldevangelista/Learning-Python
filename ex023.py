n1 = int(input("Insira qualquer número: "))

#Math way:
print("Unidade(s): {}".format(n1 % 10))
print("Dezena(s): {:.0f}".format((n1 % 100 - (n1 %10)) / 10))
print("Centena(s): {:.0f}".format((n1 % 1000 - (n1 % 100)) / 100))
print("Milhar(es): {:.0f}".format((n1 % 10000 - (n1 %1000)) / 1000))

#String Manipulation Way:
