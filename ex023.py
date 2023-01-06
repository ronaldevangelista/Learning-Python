n1 = str(input("Insira qualquer número: "))

print("Calcúlo Matemático")
# Math way:
print("Unidade(s): {}".format(int(n1) % 10))
print("Dezena(s): {:.0f}".format((int(n1) // 10 % 10)))
print("Centena(s): {:.0f}".format((int(n1) // 100 % 10)))
print("Milhar(es): {:.0f}".format((int(n1) // 1000 % 10)))

print("----x----")
print("Manipulação de String")
print("----x----")
# String Manipulation Way:
print("Unidade(s): {}".format(n1[3]))
print("Dezena(s): {}".format(n1[2]))
print("Centena(s): {}".format(n1[1]))
print("Milhares(es): {0}".format(n1[0]))
