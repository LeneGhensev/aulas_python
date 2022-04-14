import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 0
print(numero_secreto)

print("Informe o nível de dificuldade:")
nivel = int(input("(1) Fácil - (2) Médio - (3) Difícil : "))

if(nivel == 1):
    total_tentativas = 5
elif(nivel == 2):
    total_tentativas = 3
else:
    total_tentativas = 1

for rodada in range(1, total_tentativas + 1):
    print("Tentativa: {} de {}".format(rodada, total_tentativas))
    tentativa = int(input("Digite um número entre 1 e 100: "))

    if(tentativa < 1 or tentativa > 100):
        print("Você deve digitar um número entre 1 e 100! ")
        continue

    acertou = tentativa == numero_secreto
    maior = tentativa > numero_secreto
    menor = tentativa < numero_secreto

    print("Você digitou ", tentativa)

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! Seu chute foi maior.")
        elif (menor):
            print("Você errou! Seu chute foi menor.")

print("Fim de jogo!")