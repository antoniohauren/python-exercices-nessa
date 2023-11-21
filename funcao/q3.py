def comparar_numeros(numero):
    if numero == 0:
        return 0
    elif numero > 0:
        return 1
    elif numero < 0:
        return -1

print(comparar_numeros(5))
print(comparar_numeros(-2))
print(comparar_numeros(0))
    