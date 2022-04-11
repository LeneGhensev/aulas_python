print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 38
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa:", rodada, "de", total_tentativas)
    tentativa = int(input("Digite um número: "))

    acertou = tentativa == numero_secreto
    maior = tentativa > numero_secreto
    menor = tentativa < numero_secreto

    print("Você digitou ", tentativa)

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! Tente chutar um número menor.")
        elif (menor):
            print("Você errou! Tente chutar um número maior.")

    rodada = rodada + 1

print("Fim de jogo!")