# O IMC é calculado dividindo o peso pela altura ao quadrado 
# de uma pessoa. Isto é, dividir seu peso (kg) pela altura (m)
# multiplicada por ela mesma. A fórmula é a seguinte: IMC = peso/(altura x altura)
# Exercicio 1, crie um codigo que calcule o IMC
def calculoImc(peso, altura):
    imc = peso/(altura * altura)
    if imc < 16.9:
        return "Muito abaixo do peso."
    elif imc >= 17 and imc < 18.4:
        return "Abaixo do peso."
    else:
        return "Alguma coisa."