from q7 import somar_algarismos

def calcular_fatorial(numero):
    fatorial = 1

    for i in range(numero, 1, -1):
       fatorial *= i

    return fatorial

fatorial = calcular_fatorial(4)
print(somar_algarismos(fatorial))