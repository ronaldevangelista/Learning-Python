# h² = c² + c²
from math import hypot

n1 = float(input("Digite o valor do cateto oposto: "))
n2 = float(input("Digite o valor do cateto adjacente: "))

# Using basic math

hipot = (n1 ** 2 + n2 ** 2) ** (1/2)
print("\nO cateto oposto é {} e o adjacente é {}. A hipotenusa é igual a:"
      " {:.2f}".format(n1, n2, hipot))

# Using hypot from math
print("\nO cateto oposto é {} e o adjacente é {}. A hipotenusa é igual a:"
      " {:.2f}".format(n1, n2, hypot(n1, n2)))
