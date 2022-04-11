print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 38
total_tentativas = 3

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
            print("Você errou! Tente chutar um número menor.")
        elif (menor):
            print("Você errou! Tente chutar um número maior.")

print("Fim de jogo!")