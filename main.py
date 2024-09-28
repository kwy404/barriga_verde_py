nome = input("Qual o seu nome?")
notas = 0
somaFinal = 0
mediaFinal = 0
while(notas < 4):
    nota = input(f"Qual a nota que você tirou na prova {notas+1}: ")
    somaFinal += float(nota)
    notas += 1

mediaFinal = somaFinal / notas
if mediaFinal >= 7:
    print(f"Olha, {nome}. Você tirou {mediaFinal}, e você passou")
else:
    print(f"Olha, {nome}. Você tirou {mediaFinal}, e você não passou")
