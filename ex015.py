dias = int(input("O carro foi alugado por quantos dias? "))
km = float(input("Quantos quilometros foram rodados? "))
valor = float(dias * 60 + km * 0.15)
print("\nO valor a ser pago é de: {} reais".format(valor))
# improving the code.
parc = int(input("\nEm quantas parcelas você deseja pagar? "))
print("São ao todo {} parcela(s) no valor de {} reais.".format(parc, valor / parc))
