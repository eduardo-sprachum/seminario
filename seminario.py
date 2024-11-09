import random

numero_aleatorio = random.randint(1, 10)
num = int(input("Estou pensando em um número, consegue adivinhar qual? "))

while num != numero_aleatorio:
    if num > numero_aleatorio:
        print('O número sorteado é menor.')
    elif num < numero_aleatorio:
        print('O número sorteado é maior.')
    else:
        print('Você acertou o número sorteado! :)')