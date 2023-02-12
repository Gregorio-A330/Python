print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # string interpolation
    
    chute_str = input("Digite o seu numero: ")
    chute = int(chute_str)

    print("você digitou ", chute_str, type(chute_str)) ## input retorna a entrada como string e é necessário converter

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


# Diferenças entre python 2 e python 3 para >>>>> print e input()
#  não tinha obrigatoriedade de parenteses no python 2 e o print do 3 aceita mais parametros como o sep="" e o end=""
#  não converte diretamente o input no python 3 porque no python 2 era considerado má pratica

# raw_input só exite no python 2 e trazia a entrada diretamente sem conversão não existe no python 3


# elif -> else if()


    #  for VARIAVEL in range(inicio, final, steps?):
    #   ou for VARIAVEL in [1,2,3,4,5] 
    #  o valor final não faz parte é exclusivoo


# for rodada in range(1,10):
#     print(rodada)