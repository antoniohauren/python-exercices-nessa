i = 0

inpares_para_mostrar = int(input("Digite um valor: "))
numeros_impares_encontrados = 0

while numeros_impares_encontrados < inpares_para_mostrar:
    if i % 2 != 0:
        print(i)
        numeros_impares_encontrados += 1

    i += 1