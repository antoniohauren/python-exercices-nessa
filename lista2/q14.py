numero_inteiro = input("Digite um número inteiro: ")

if len(numero_inteiro) != 3:
    print("Número inválido")

else:
    print("numero lido: ", numero_inteiro, "\nnumero gerado: ", numero_inteiro[2], numero_inteiro[1], numero_inteiro[0], sep='')
