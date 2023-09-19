salario = float(input("Digite o salário: "))
prestacao = float(input("Digite o valor da prestação: "))

prestacao_porcentagem = (prestacao / salario) * 100

if prestacao_porcentagem > 20:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
