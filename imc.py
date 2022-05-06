def get_positive_float_input(msg):
    input_float = 0
    is_positive_float = False
    
    while is_positive_float is False:
        input_str = input(msg)
        try:
            input_float = float(input_str)
            if input_float < 0:
                print('Por favor, digite um número positivo')
            else:
                is_positive_float = True
        except ValueError:
            print('Por favor, digite um número positivo')    
    
    return input_float


def get_positive_int_input(msg):
    input_int = 0
    is_positive_int = False
    
    while is_positive_int is False:
        input_str = input(msg)
        try:
            input_int = int(input_str)
            if input_int < 0 and input_str.index('.') >= 0:
                print('Por favor, digite um número inteiro positivo')
            else:
                is_positive_int = True
        except ValueError:
            print('Por favor, digite um número inteiro positivo')    
    
    return input_int

def get_sexo_input():
    msg = '\nDigite seu sexo. Mulher (M) / Homem (H): '
    input_sexo = input(msg)
    while input_sexo != 'M' and input_sexo != 'H':
        print("Por favor, digite 'M' ou 'H'")
        input_sexo = input(msg)
    return input_sexo

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

def calculo_calorias(sexo, peso, idade):
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
    return calorias_diarias * fator_atividade

print()
print('-' * 50)
print('Cálculo IMC\n')

altura = get_positive_float_input('\nDigite sua altura em CM: ')
peso = get_positive_float_input('\nDigite seu peso em Kg: ')

res_imc = calculo_imc(altura, peso)
classificacao_imc = classifica_imc(res_imc)

print('\nTabela de IMC da OMS (https://bvsms.saude.gov.br/bvs/dicas/215_obesidade.html)')
print(' - Menor que 18,5 - Abaixo do peso')
print(' - Entre 18,5 e 24,9 - Peso normal')
print(' - Entre 25 e 29,9 - Sobrepeso')
print(' - Igual ou acima de 30 - Obesidade\n')

print('Seu IMC: %.2f' % res_imc)
print('Segundo a tabela da OMS, seu IMC está classificado como:', classificacao_imc)

print()
print('-' * 50)
print('Cálculo Calorias\n')

idade = get_positive_int_input('\nDigite sua idade: ')
sexo = get_sexo_input()

print('\nTabela de calorias diárias (https://www.tuasaude.com/como-calcular-o-gasto-calorico/)\n')
print('{0: <15} {1: <30} {2: <30}'.format('Idade', 'Mulher', 'Homem'))
print('{0: <15} {1: <30} {2: <30}'.format('0 a 3 anos', '(58,317 x peso em kg) – 31,1', '(59,512 x peso em kg) – 30,4'))
print('{0: <15} {1: <30} {2: <30}'.format('3 a 10 anos', '(20,315 x peso em kg) + 485,9', '(22,706 x peso em kg) + 504,3'))
print('{0: <15} {1: <30} {2: <30}'.format('10 a 18 anos', '(13,384 x peso em kg) + 692,6', '(17,686 x peso em kg) + 658,2'))
print('{0: <15} {1: <30} {2: <30}'.format('18 a 30 anos', '(14,818 x peso em kg) + 486,6', '(15,057 x peso em kg) + 692,2'))
print('{0: <15} {1: <30} {2: <30}'.format('30 a 60 anos', '(8,126 x peso em kg) + 845,6', '(11,472 x peso em kg) + 873,1'))
print('{0: <15} {1: <30} {2: <30}'.format('≥ 60 anos', '(9,082 x peso em kg) + 658,5', '(11,711 x peso em kg) + 587,7'))

total_calorias = calculo_calorias(sexo, peso, idade)
print('\nDe acordo com a tabela, a quantidade de calorias que voce deve ingerir diáriamente é de: %.2f' % total_calorias)

escolha_menu = ''
while escolha_menu != '9':

    caloria_ingerida = get_positive_float_input('\nDigite o total de caloria ingerida na refeição: ')
    total_calorias -= caloria_ingerida

    print('\nVocê tem %.2f calorias ainda para ingerir.\n\n' % total_calorias)

    print('1 - Continuar com o cálculo')
    print('9 - Sair do programa')
    escolha_menu = input('\nEscolha uma das opções: ')
