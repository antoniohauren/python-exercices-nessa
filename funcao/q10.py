
def main(x, z):
    potencia = 1

    for i in range(0, z):
        potencia *= x

    return potencia

print(main(2,5))
print(main(5,10))

# i = 1 == potencia = 1 * 2 = 2
# i = 1 == potencia = 2 * 2 = 4
# i = 2 == potencia = 4 * 2 = 8
# i = 3 == potencia = 8 * 2 = 16
# i = 4 == potencia = 16 * 2 = 32
