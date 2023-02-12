import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

# numero_secreto = round(random.random() * 100) 
numero_secreto = random.randrange(1,101) 
total_de_tentativas = 3

# numero_random = random.random() * 100
# int(numero_random)

print(numero_secreto)


for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # string interpolation
    
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    print("você digitou ", chute_str, type(chute_str)) ## input retorna a entrada como string e é necessário converter

    if(chute < 1 or chute > 100):
        print("você deve digitar um número entre 1 e 100!")
        continue #retorna pro inicio do for

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):  # o dois pontos é inicio de um bloco de execução
    # if (int(chute_str) == numero_secreto):  # OU
        print("voce acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")


print("Fim de jogo...")