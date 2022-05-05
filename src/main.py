import caloria, imc

def main():
    '''
    Função que vai ser invocada como principal. 
    É nela que vai ter a lógica de integraçao das outras funções auxiliares
    '''
    res_imc = imc.calculo_imc()
    res_cal = caloria.calculo_calorias()

if __name__ == '__main__':
    main()