def somar_algarismos(numero):
    if type(numero) != int or numero < 0:
        return 'Número Inválido'

    numero_string = str(numero)

    soma = 0

    for algarismo in numero_string:
        soma += int(algarismo)

    return soma

if __name__ == '__main__':
    print(somar_algarismos('23'))
    print(somar_algarismos(-2))
    print(somar_algarismos(13))
    print(somar_algarismos(251))