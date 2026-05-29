def converter_altura_para_metros(altura_cm: float) -> float:
    return altura_cm / 100


def calcular_imc(peso: float, altura_metros: float) -> float:
    return peso / (altura_metros * altura_metros)


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"


def main():
    print("Calculadora de IMC - Sprint 2")

    peso = float(input("Introduza o seu peso em kg: "))
    altura_cm = float(input("Introduza a sua altura em centímetros: "))

    altura_metros = converter_altura_para_metros(altura_cm)
    imc = calcular_imc(peso, altura_metros)
    classificacao = classificar_imc(imc)

    print(f"O valor do IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")


main()