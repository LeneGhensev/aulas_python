print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 38

tentativa = int(input("Digite um número: "))

print("Você digitou ", tentativa)

if(tentativa == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")