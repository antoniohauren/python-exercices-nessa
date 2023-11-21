i = 0

while i < 10:
    valor = float(input("Digite um valor:"))

    if i == 0:
        menor = valor
        maior = valor

    if (valor > maior):
        maior = valor

    if (valor < menor):
        menor = valor

    i += 1

print("O maior valor eh: ", maior, "O menor valor eh: ", menor)