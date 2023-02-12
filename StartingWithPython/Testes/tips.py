
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


#  or ----- and 



# Mais exemplos, sempre comparando o Python 2 com Python 3, existem no link: https://pyformat.info/

# TEMPLATE STRING PARECIDO COM JS

# No Python 3.6+
# A partir da versão 3.6 do Python, foi adicionado um novo recurso para realizar a interpolação de strings. Esse recurso é chamado de f-strings ou formatted string literals.

# Esse recurso funciona da seguinte forma. Vamos imaginar que temos uma variável nome:

# >>> nome = 'Matheus'
# >>> print(f'Meu nome é {nome}')
# Meu nome é MatheusCOPIAR CÓDIGO
# Quando colocamos a letra f antes das aspas, informamos ao Python que estamos utilizando uma f-string. Dessa forma o Python consegue, em tempo de execução, captar a expressão que está entre chaves ({ }) e avaliá-la.

# Além de variáveis, podemos passar também de funções e métodos:

# >>> nome = 'Matheus'
# >>> print(f'Meu nome é {nome.lower()}')
# Meu nome é matheus


# python builtIn -> funções já imbutidas
