lado_a = int(input("Lado A: "))
lado_b = int(input("Lado B: "))
lado_c = int(input("Lado C: "))

if lado_a < (lado_b + lado_c) and lado_b < (lado_a + lado_c) and lado_c < (lado_a + lado_b):
    if lado_a == lado_b == lado_c:
        print("Triangulo Equilatero")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("Triangulo Isósceles")
    elif lado_a != lado_b != lado_c:
        print("Triangulo Escaleno")

else:
    print("Não é um triângulo")