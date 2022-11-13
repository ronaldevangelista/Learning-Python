from math import floor

n1 = float(input("Digite um número real: "))

# Using basic math:
print("O número {} tem a parte inteira {:.0f}.".format(n1, n1 // 1))

# Importing Floor from math:
print("\nO número {} tem a parte inteira {}.".format(n1, floor(n1)))
