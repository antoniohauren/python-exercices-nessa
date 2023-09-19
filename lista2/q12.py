salario = float(input('Digite o salário: '))

# aumento = 1 + (21.37 / 100)
# novo_salario = salario * aumento

aumento = (21.37 / 100) # 21.37%
novo_salario = salario + (salario * aumento) # salario + valor aumentado

print('O novo salario do funcionario eh: ', novo_salario)

