import random

# Declaração de funções com def
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # numero_secreto = round(random.random() * 100) 
    numero_secreto = random.randrange(1, 101) 
    total_de_tentativas = 0
    # numero_random = random.random() * 100
    # int(numero_random)
    pontos = 1000

    print("Qual o nivel de dificultade?")
    print("(1) Facil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível:"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

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
            print("voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim de jogo...")


# caso execute o arquivo diretamente sem ser pelo import ele atribui a esta variavel __name__ a informação __main__ e informa que é um arquivo executado diretamente
if(__name__ == "__main__"):
    jogar()