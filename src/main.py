import caloria, imc

def get_input_numerico(msg):
    input_str = input(msg)

    while not input_str.replace('.', '').isdigit():
        print('Por favor digite um número')
        input_str = input(msg)
    
    return float(input_str)

def main():
    '''
    Função que vai ser invocada como principal. 
    É nela que vai ter a lógica de integraçao das outras funções auxiliares.
    '''
    altura = get_input_numerico('\nDigite sua altura: ')
    peso = get_input_numerico('\nDigite seu peso: ')

    res_imc = imc.calculo_imc(altura, peso)
    classificacao_imc = imc.classifica_imc(res_imc)

    print('\nTabela de IMC da OMS (https://bvsms.saude.gov.br/bvs/dicas/215_obesidade.html)')
    print(' - Menor que 18,5 - Abaixo do peso')
    print(' - Entre 18,5 e 24,9 - Peso normal')
    print(' - Entre 25 e 29,9 - Sobrepeso')
    print(' - Igual ou acima de 30 - Obesidade\n')

    print('Seu IMC:', res_imc)
    print('Segundo a tabela da OMS, seu IMC está classificado como:', classificacao_imc)

if __name__ == '__main__':
    main()