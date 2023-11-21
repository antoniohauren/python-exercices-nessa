numero = int(input("Digite o numero positivo: "))
mensagem = "Estou sabendo Programar haha"

if numero < 0:
    print("Numero invalido")
else:
    i = 1
    while i <= numero:
        print(i, mensagem)
        i = i + 1
