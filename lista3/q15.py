import math

a = int(input("Digite o A: "))
b = int(input("Digite o B: "))
c = int(input("Digite o C: "))

if a == 0:
    print("Não é uma equação de segundo grau")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Nao existe raiz real")
    elif delta == 0:
        print("Raiz unica")
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a

        print("raiz 1:", x1, "raiz 2", x2)
