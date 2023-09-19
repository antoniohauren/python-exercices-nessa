nota1 = float(input("Digite a nota 1: "))
if nota1 < 0 or nota1 > 10:
    print("Nota 1 inválida")
    quit()

nota2 = float(input("Digite a nota 2: "))
if nota2 < 0 or nota2 > 10:
    print("Nota 2 inválida")
    quit()

nota3 = float(input("Digite a nota 3: "))
if nota3 < 0 or nota3 > 10:
    print("Nota 3 inválida")
    quit()

media = (nota1 + nota2 + nota3) / 3

# https://docs.python.org/3/tutorial/inputoutput.html
print("a media das notas eh: {:.2f}".format(media))
