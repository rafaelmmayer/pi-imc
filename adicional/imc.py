peso = 0

def calculo_imc(altura, peso):
    altura /= 100
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

def calculo_calorias(sexo, idade):
    global peso
    calorias_diarias = 0
    if idade <= 3:
        if sexo == 'M':
            calorias_diarias = 58.317 * peso - 31
        else:
            calorias_diarias = 59.512 * peso - 30.4
    elif idade > 3 and idade <= 10:
        if sexo == 'M':
            calorias_diarias = 20.315 * peso + 485.9
        else:
            calorias_diarias = 22.706 * peso + 504.3
    elif idade > 10 and idade <= 18:
        if sexo == 'M':
            calorias_diarias = 13.384 * peso + 692.6
        else:
            calorias_diarias = 17.686 * peso + 658.2
    elif idade > 18 and idade <= 30:
        if sexo == 'M':
            calorias_diarias = 14.818 * peso + 486.6
        else:
            calorias_diarias = 15.057 * peso + 692.2
    elif idade > 30 and idade <= 60:
        if sexo == 'M':
            calorias_diarias = 8.126 * peso + 845.6
        else:
            calorias_diarias = 11.472 * peso + 873.1
    else:
        if sexo == 'M':
            calorias_diarias = 9.082 * peso + 658.5
        else:
            calorias_diarias = 11.711 * peso + 587.7

    fator_atividade = 1.55 # Menor fator
    return round(calorias_diarias * fator_atividade, 2)

def calcular_imc(*args, **kwargs):
    global peso
    altura = int(document.getElementById('inputAltura').value)
    peso = int(document.getElementById('inputPeso').value)
    imc = calculo_imc(altura, peso)
    classificacao_imc = classifica_imc(imc)
    pyscript.write('spanResultadoImc', f'IMC: {imc}')
    pyscript.write('spanClassificacaoImc', classificacao_imc)


def calcular_calorias(*args, **kwargs):
    sexo = document.querySelector('input[name="sexos"]:checked').value
    idade = int(document.getElementById('inputIdade').value)
    total_calorias = calculo_calorias(sexo, idade)
    pyscript.write('spanTotalCalorias', total_calorias)


def calcular_refeicao(*args, **kwargs):
    refeicao = float(document.getElementById('inputRefeicao').value)
    textRefeicao = document.getElementById('spanRefeicao').innerText
    calorias_restante = 0
    if textRefeicao:
        float_refeicao = float(textRefeicao)
        calorias_restante = float_refeicao - refeicao
    else:
        spanTotalCalorias = float(document.getElementById('spanTotalCalorias').innerText)
        calorias_restante = spanTotalCalorias - refeicao
    if calorias_restante < 0:
        calorias_restante = 0
    pyscript.write('spanRefeicao', round(calorias_restante, 2))
    document.getElementById('inputRefeicao').value = ''
