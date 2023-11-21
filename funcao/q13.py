def desenhar(numero_linhas):
    simbolo = '!'

    if type(numero_linhas) != int or numero_linhas < 0:
        return print('Número Inválido')

    for i in range(numero_linhas):
        # print(simbolo * (i + 1))
        for j in range(i + 1):
            print(simbolo, end='')

        print()

desenhar(-1)
desenhar('123')
desenhar(5)