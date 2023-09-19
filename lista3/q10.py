numero1 = float(input("Digite o 1o numero: "))
numero2 = float(input("Digite o 2o numero: "))


operacao = int(input("Digite a operacao: "))

if operacao == 1:
    media = (numero1 + numero2) / 2
    print("Media:", media)
elif operacao == 2:
    if numero1 > numero2:
        print("Diferenca:", numero2 - numero1)
    else:
        print("Diferenca:", numero1 - numero2)
elif operacao == 3:
    print("Produto:", numero1 * numero2)

elif operacao == 4:
    if numero2 == 0:
        print("Divisao por zero")
    else:
        print("Divisao:", numero1 / numero2)
