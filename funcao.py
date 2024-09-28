import imc as util
# Criem uma função que pergunta
# ao usuario qual o nome dele, e que idade
# Ele, o peso e altura, e faça o
# calculo o do imc aqui dentro
def apresentacao(nome, idade, peso, altura):
    calculo = util.calculoImc(peso, altura)
    print(f"{nome} está {calculo}")

nome = input("Qual seu nome? ")

apresentacao(nome, 25, 80, 1.90)