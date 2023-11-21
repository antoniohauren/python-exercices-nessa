i = 0
soma = 0

while i < 10:
    valor = int(input("Digite um valor: "))

    if valor > 0:
        soma = soma + valor
        i += 1

media = soma / 10

print("A média dos valores positivos é: ", media)
