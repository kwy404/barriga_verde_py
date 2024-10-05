# Crie uma função que é um while que pergunta varios nomes e calcula
# a idade + 10 anos. sleep, quantos segundos você quer esperar
# para perguntar novammente

# Crie um cadastro de usuario
# Nome, sobrenome, usuario e senha
# 1 para logar, 1 para registro, 2 para sair
# dentro de um while
# Se ele tiver registrado, atualizar a conta
# E pedir para logar, somente com usuario e senha


global nome
global sobrenome
global usuario
global senha

nome = ""
sobrenome = ""
usuario = ""
senha = ""

def login(nome_, sobrenome_, usuario_, senha_):
    print(nome)

def registroOuAtualizar(nome_, sobrenome_, usuario_, senha_):
    global nome
    global sobrenome
    global usuario
    global senha
    nome = nome_
    sobrenome = sobrenome_
    usuario = usuario
    senha = senha

if usuario != "" or senha != "":
    opcao = int("Insira 1 para login ou 2 para para atualizar registro\n")
else:
    opcao = int("Insira 1 para login ou 2 para para cadastrar\n")
    
if opcao == 1:
    
    login()