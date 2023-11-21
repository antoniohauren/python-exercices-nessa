def eh_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def proximo_numero_primo(numero):
    numero += 1

    while True:
        if eh_primo(numero):
            return numero
        else:
            numero += 1


def maior_fator_primo(numero):
    maior_fator = -1
    primo = 1

    while numero != 1:
        primo = proximo_numero_primo(primo)

        while numero % primo == 0:
            maior_fator = primo
            numero /= primo
    
    return maior_fator

if __name__ == '__main__':
    print(maior_fator_primo(220))