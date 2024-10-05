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

def chamarNome(nome, sobrenome):
    print(f"{nome} {sobrenome}")

chamarNome("Alexandre", "Silva")

# Crie uma função que some 2 numeros e divide por 3, e use return

# Crie uma função que faça conversão de fareheitn para celsius

# Crie uma função que faça conversão de Celsius para fareheitn

# Crie uma função que usa função auxiliares, por exemplo
# Uma função que busca o nome, e calcula a idade pelo ano que ela nasceu

# Faça um programa com funções que simule um banco, com funcoes de deposito, saque
# Validacao que tenha dinheiro para saque. Deixe algo pratico, coloque opcoes, 1 para saque
# 2 para deposito, 3 para visualizar historico e 4 para sair do programa
# para sair do while, se usa o break
historico = ""
condicao = True
while(condicao):
    opcao = input("Qual opção")
    if(opcao == 1):
        historico += "Você sacou tal valor $\n"
    break

#