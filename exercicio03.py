# Início da função metragemLimpeza()

def metragemLimpeza():
    print('-------------------- Menu 1 de 3 - Metragem Limpeza --------------------')
    while True:
        try:
            metragemL = int(input('Entre com a metragem da casa (m²): '))
            if (metragemL >= 30) and (metragemL < 300):  # Entre 30 e 299, contrata 1 pessoa e faz o calculo do valor
                print('É necessário contratar 1 pessoa')
                return 60 + (0.3 * metragemL)
            elif (metragemL >= 300) and (
                    metragemL < 700):  # Entre 300 e 699, contrata 2 pessoa e faz o calculo do valor
                print('É necessário contratar 2 pessoas')
                return 120 + (0.5 * metragemL)
            else:
                print('Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !')
                continue  # Retorna para o início do While
        except ValueError:  # Caso o usuário digitar letra ou float, mostra uma mensagem de aviso.
            print('Pare de digitar valores não inteiros.')

# Fim da função metragemLimpeza()


# Início da função tipoLimpeza()

def tipoLimpeza():
    print('-------------------- Menu 2 de 3 - Tipo de Limpeza --------------------')
    while True:
        tipoL = input('Qual tipo de limpeza você deseja? \n' +
                      'B – Básica - Indicada para sujeiras semanais ou quinzenais \n' +
                      'C – Completa - (30% a mais) Indicada para sujeiras antigas e/ou não rotineiras \n' +
                      '>> ')

        tipoL = tipoL.upper()  # Concertar problema de letra minuscula
        tipoL = tipoL.strip()  # Concertar problema de espaçamento
        if tipoL == 'B':  # Se o usuário digitar essa opção, a multiplicação será usada no final do codigo
            return 1.00
        elif tipoL == 'C':  # Se o usuário digitar essa opção, a multiplicação será usada no final do codigo
            return 1.30
        else:
            print('Opções diferentes de B/C não existem... Por favor escolha uma entre as duas opções')  # Para caso
            # o usuário não digitar nenhuma das 2 opções
            continue  # Volta ao início do laço While

# Fim da função tipoLimpeza()


# Início da função adicionalLimpeza()

def adicionalLimpeza():
    print('-------------------- Menu 3 de 3 - Adicionais da Limpeza --------------------')
    acumulador = 0  # Usado para soma o valor dos adicionais
    while True:  # Escolha dos adicionais
        adicionaL = input('Deseja mais algum adicional? \n' +
                                '0- Não desejo mais nada (encerrar) \n' +
                                '1- Passar 10 peças de roupas - R$ 10.00 \n' +
                                '2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                                '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                                '>> ')
        if adicionaL == '0':
            return acumulador
        elif adicionaL == '1':
            acumulador = acumulador + 10
            continue  # Volta para a pergunta "Deseja mais algum adicional"
        elif adicionaL == '2':
            acumulador = acumulador + 12
            continue  # Volta para a pergunta "Deseja mais algum adicional"
        elif adicionaL == '3':
            acumulador = acumulador + 20
            continue  # Volta para a pergunta "Deseja mais algum adicional"
        else:
            print('Opções diferentes de 0/1/2/3 não existem... Por favor escolha uma entre as opções')  # Para caso
            # o usuário digitar nenhuma das opções
            continue  # Volta para a pergunta "Deseja mais algum adicional"

# Fim da função adicionalLimpeza()

# Início da Main

print('Bem-vindo ao Programa de Serviços de Limpeza do João Pedro Flauzino Nascimento')  # Identificador

metragem = metragemLimpeza()
tipo = tipoLimpeza()
adicional = adicionalLimpeza()

total = (metragem * tipo) + adicional  # Calculo para saber o valor total

print('TOTAL: R$ {:.2f} (Metragem: R$ {:.2f}, Tipo: R$ {:.2f}, Adicional: R$ {:.2f})'.format(total, metragem, tipo, adicional))
