valor_positivo = int(input("Digite um valor positivo: "))

if valor_positivo < 0:
    print("O valor digitado não é positivo!")
else:
    horas = valor_positivo // 3600
    valor_positivo = valor_positivo % 3600

    minutos = valor_positivo // 60
    valor_positivo = valor_positivo % 60

    segundos = valor_positivo

    print(horas, minutos, segundos)