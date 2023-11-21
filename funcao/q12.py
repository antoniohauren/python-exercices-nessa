from q11 import eh_primo

def n_primos(numero):
    quantidade_de_primos = 0

    for i in range(numero, 2, -1):
        if eh_primo(i):
            quantidade_de_primos += 1

    return quantidade_de_primos

if __name__ == '__main__':
    print(n_primos(15))