valor = float(input("Valor em reais: "))

# valor_restante = valor

ganhador1 = valor * (46/100)
# valor_restante = valor_restante - ganhador1

ganhador2 = valor * (32/100)
# valor_restante = valor_restante - ganhador2

# ganhador3 = valor_restante
ganhador3 = valor - (ganhador1 + ganhador2)

print(ganhador1, ganhador2, ganhador3)