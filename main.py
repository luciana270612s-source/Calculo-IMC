print("Calculadora de IMC")

peso = float(input("Introduza o seu peso em kg: "))
altura_cm = float(input("Introduza a sua altura em centímetros: "))

altura_metros = altura_cm / 100

imc = peso / (altura_metros * altura_metros)

print(f"O valor do IMC é: {imc:.2f}")

if imc < 18.5:
    print("Fora do peso normal")
elif imc < 25:
    print("Peso normal")
else:
    print("Fora do peso normal")