numero1 = int(input("Digite o 1o numero: "))
numero2 = int(input("Digite o 2o numero: "))

if numero1 == numero2:
    print("Os numeros sao iguais")
elif numero2 > numero1:
    print("O maior numero eh:", numero2)
elif numero1 > numero2:
    print("O maior numero eh:", numero1)