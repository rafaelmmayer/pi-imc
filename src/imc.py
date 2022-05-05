def calculo_imc(altura, peso):
    imc = peso/(altura*altura)
    return round(imc, 2)

def classifica_imc(imc):
    if imc <= 18.5:
        return 'Abaixo do peso'
    elif imc > 18.5 and imc <= 24.9:
        return 'Peso normal'
    elif imc > 25 and imc <= 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidade'