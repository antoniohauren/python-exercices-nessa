valor_premio = float(input("Digite o valor do prêmio: "))

amigo1 = float(input("Digite o valor que o amigo 1 contribuiu: "))
amigo2 = float(input("Digite o valor que o amigo 2 contribuiu: "))
amigo3 = float(input("Digite o valor que o amigo 3 contribuiu: "))

total = amigo1 + amigo2 + amigo3

amigo1_porcentagem = (amigo1 / total)
amigo2_porcentagem = (amigo2 / total)
amigo3_porcentagem = (amigo3 / total)

amigo1_ganhos = amigo1_porcentagem * valor_premio
amigo2_ganhos = amigo2_porcentagem * valor_premio
amigo3_ganhos = amigo3_porcentagem * valor_premio

print(amigo1_ganhos, amigo2_ganhos, amigo3_ganhos)
