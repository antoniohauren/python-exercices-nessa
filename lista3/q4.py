valor1 = int(input('Digite o 1o valor: '))
valor2 = int(input('Digite o 2o valor: '))
valor3 = int(input('Digite o 3o valor: '))

if valor1 == valor2 and valor1 == valor3:
    print('Os valores são iguais')
    
elif valor1 >= valor2 and valor1 >= valor3:
    print('O maior valor é: ', valor1)

elif valor2 > valor1 and valor2 >= valor3:
    print('O maior valor é: ', valor2)

elif valor3 >= valor1 and valor3 >= valor2:
    print('O maior valor é: ', valor3)