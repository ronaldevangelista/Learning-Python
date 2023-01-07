print("Passando no radar...")
km = float(input("insira a velocidade do seu carro: "))

from time import sleep
print("CARREGANDO...")
sleep(4)


if km > 80:
    multa = float((km - 80) * 7)
    print("Você foi MULTADO por andar a {}Km/h!".format(km))
    print("O valor da multa é de: {} reais!".format(multa))
else:
    print("Você é um motorista consciente!")
    print("Pode seguir normalmente!")
