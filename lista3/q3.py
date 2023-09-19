numero1 = int(input("Digite o 1o numero: "))
numero2 = int(input("Digite o 2o numero: "))
numero3 = int(input("Digite o 3o numero: "))
numero4 = int(input("Digite o 4o numero: "))

soma = 0

if numero1 % 2 == 0:
    soma = soma + numero1
if numero2 % 2 == 0:
    soma = soma + numero2
if numero3 % 2 == 0:
    soma = soma + numero3
if numero4 % 2 == 0:
    soma = soma + numero4

print('A soma dos numeros pares eh:', soma)