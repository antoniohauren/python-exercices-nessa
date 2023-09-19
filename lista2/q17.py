# import math

coordenada_x = int(input("Digite o valor de x: "))
coordenada_y = int(input("Digite o valor de y: "))

ponto1 = coordenada_x ** 2
ponto2 = coordenada_y ** 2

# distancia = math.sqrt(ponto1 + ponto2)
distancia = (ponto1 + ponto2) ** (1/2)

print(distancia)
