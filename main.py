print("Calculadora de IMC")

print("Calculadora de IMC")

peso = float(input("Introduza o seu peso em kg: "))
altura = float(input("Introduza a sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"O seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Excesso de peso")
elif imc < 35:
    print("Classificação: Obesidade grau I")
elif imc < 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")