def soma_entre_numeros(numero1, numero2):
    if type(numero1) != int or numero1 < 0:
        return 'Número 1 Inválido'
    if type(numero2) != int or numero2 < 0:
        return 'Número 2 Inválido'
    
    menor = 0
    maior = 0
    soma = 0

    if numero1 < numero2:
        menor = numero1
        maior = numero2
    else:
        menor = numero2
        maior = numero1
    
    for numero in range(menor + 1, maior):
        soma += numero

    return soma

print(soma_entre_numeros('1',2))
print(soma_entre_numeros(1,'2'))
print(soma_entre_numeros(10,15))