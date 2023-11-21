def e_quadrado_perfeito(numero):
    if type(numero) != int:
        return False

    if numero < 0:
        return False
    
    for i in range(numero, 0, -1):
        if i * i == numero:
            return True


print(e_quadrado_perfeito(2.5))
print(e_quadrado_perfeito('25'))
print(e_quadrado_perfeito(1))
print(e_quadrado_perfeito(4))
print(e_quadrado_perfeito(9))
print(e_quadrado_perfeito(25))