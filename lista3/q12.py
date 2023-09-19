numero = int(input("Digite o numero da semana: "))

if numero > 7 or numero < 1:
    print("Numero invalido, 1~7")

elif numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda")
elif numero == 3:
    print("Terca")
elif numero == 4:
    print("Quarta")
elif numero == 5:
    print("Quinta")
elif numero == 6:
    print("Sexta")
elif numero == 7:
    print("Sabado")