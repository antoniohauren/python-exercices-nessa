numero = int(input("Digite um numero: "))

por3 = False
por5 = False

if numero % 3 == 0:
    por3 = True

if numero % 5 == 0:
    por5 = True

if por3 and not por5:
    print("Divisivel por 3")

if por5 and not por3:
    print("Divisivel por 5")

if por3 and por5:
    print("Divisivel por 3 e 5")
