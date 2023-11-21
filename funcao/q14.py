def desenhar_triangulo(numero):
    largula = numero
    altura = 2 * numero - 1

    for i in range(altura):
        if i < largula:
            print((i + 1) * '*')
        else:
            print((altura - i) * '*')

desenhar_triangulo(4)