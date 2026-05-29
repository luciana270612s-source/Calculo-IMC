print("Calculadora de IMC")

peso = float(input("Introduza o seu peso em kg: "))
altura = float(input("Introduza a sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"O seu IMC é: {imc:.2f}")