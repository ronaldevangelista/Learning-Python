from random import choice

n1 = input("Adicione o nome do primeiro aluno: ")
n2 = input("Adicione o nome do segundo aluno: ")
n3 = input("Adicione o nome do terceiro aluno: ")
n4 = input("Adicione o nome do quarto aluno: ")

lista = [n1, n2, n3, n4]

print("O professor selecionou o(a) {} para apagar o quadro".format(choice(lista)))
