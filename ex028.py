from random import randint
from time import sleep
print("Seja bem-vindo jogador.")
print("-=-=-=-=X=-=-=-=-")
print("Neste momento estamos sorteando um número de 0 a 5.")
sleep(3)
valor = int(randint(0, 5))
print("Valor sorteado!")
print("-=-=-=-=X=-=-=-=-")

aposta = int(input("Qual número inteiro de 0 a 5 é sua aposta? "))
print("-=-=-=-=X=-=-=-=-")

if aposta == valor:
    print("Parabéns, você acertou!")
else:
    print("Que peninha. Tente novamente!")

print("O valor era: {}".format(valor))
