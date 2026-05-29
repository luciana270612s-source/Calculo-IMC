def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)


print("Calculadora de IMC")

continuar = "s"

while continuar.lower() == "s":
    peso = float(input("Introduza o seu peso em kg: "))
    altura = float(input("Introduza a sua altura em metros: "))

    imc = calcular_imc(peso, altura)

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

    continuar = input("\nDeseja calcular novamente? (s/n): ")

print("\nPrograma terminado.")