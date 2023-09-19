valor1 = int(input('Digite o 1o valor: '))
valor2 = int(input('Digite o 2o valor: '))
valor3 = int(input('Digite o 3o valor: '))

if valor1 <= valor2 <= valor3:
    print(valor1, valor2, valor3)

elif valor1 <= valor3 <= valor2:
    print(valor1, valor3, valor2)

elif valor2 <= valor3 <= valor1:
    print(valor2, valor3, valor1)

elif valor2 <= valor1 <= valor3:
    print(valor2, valor1, valor3)

elif valor3 <= valor2 <= valor1:
    print(valor3, valor2, valor1)

elif valor3 <= valor1 <= valor2:
    print(valor3, valor1, valor2)
