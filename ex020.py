from random import sample

n1 = input("Insira o nome do primeiro aluno: ")
n2 = input("Insira o nome do segundo aluno: ")
n3 = input("Insira o nome do terceiro aluno: ")
n4 = input("Insira o nome do quarto aluno: ")

lista = [n1, n2, n3, n4]

print("A ordem que o professor escolheu para realizar a tarefa é a seguinte:")
print(sample(lista, k=4))
