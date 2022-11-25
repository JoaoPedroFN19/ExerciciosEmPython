# Início das Variáveis Globais
listaFuncionario = []
codigoFuncionario = 0


# Fim das Variáveis Globais

# Início de cadastrarFuncionario
def cadastrarFuncionario(codigo):
    print('-------------------- MENU CADASTRAR FUNCIONÁRIO --------------------')
    print('Código do FUNCIONÁRIO: {}'.format(codigo))
    nome = input('Por favor, entre com o NOME: ')
    setor = input('Por favor, entre com o SETOR: ')
    salario = float(input('Por favor, entre com o SALÁRIO (R$): '))
    dicionarioFuncionario = {'codigo': codigo,  # Dicionario para guardar as informações  codigo, nome, setor e salario
                             'nome': nome,
                             'setor': setor,
                             'salario': salario}
    listaFuncionario.append(dicionarioFuncionario.copy())


# Fim de cadastrarFuncionario

# Início de consultarFuncionario
def consultarFuncionario():
    while True:
        print('-------------------- MENU CONSULTAR FUNCIONÁRIO --------------------')
        opcaoConsultar = input('Escolha a opção desejada: \n' +  # Opções para consulta
                               '1 - Consultar Todos os Funcionários \n' +
                               '2 - Consultar Funcionário por Id \n' +
                               '3 - Consultar Funcionário(s) por Setor \n' +
                               '4 - Retornar \n' +
                               '>> ')
        if opcaoConsultar == '1':
            print(' Você escolheu a opção Consultar Todos os Funcionários ')
            print('-------------------------------------------------------')
            for funcionario in listaFuncionario:
                for key, value in funcionario.items():  # Varrer todos os conjuntos chave e valor do dicionario
                    # funcionario
                    print(' {}: {}'.format(key, value))

        elif opcaoConsultar == '2':
            print(' Você escolheu a opção Consultar Funcionário por Id ')
            print('----------------------------------------------------')
            valorDesejado = int(input('Digite o ID do Funcionário: '))
            for funcionario in listaFuncionario:
                if funcionario['codigo'] == valorDesejado:  # Busca especifica pelo codigo dos funcionario
                    print('----------------------------------------------------')
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))

        elif opcaoConsultar == '3':
            print(' Você escolheu a opção Consultar Funcionário(s) por Setor ')
            print('----------------------------------------------------------')
            valorDesejado = input('Digite o SETOR do(s) Funcionário(s): ')
            for funcionario in listaFuncionario:
                if funcionario['setor'] == valorDesejado:  # Busca especifica pelo setor dos funcionario
                    print('-------------------------------------------------')
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))

        elif opcaoConsultar == '4':
            return

        else:
            print('Opção Inválida...')
            continue


# Fim de consultarFuncionario

# Início de removerFuncionario
def removerFuncionario():
    print('-------------------- MENU REMOVER FUNCIONÁRIO --------------------')
    valorDesejado = int(input('Digite o CÓDIGO do Funcionário que deseja remover: '))
    for funcionario in listaFuncionario:
        if funcionario['codigo'] == valorDesejado:
            listaFuncionario.remove(funcionario)
            print('Funcionário Removido!')

# Fim de removerFuncionario

# Início da Main
print('Bem-Vindo ao Controle de Funcionários do João Pedro Flauzino Nascimento')
while True:
    print('-------------------- MENU PRINCIPAL --------------------')
    opcaoPrincipal = input('Escolha a opção desejada: \n' +
                           '1 - Cadastrar Funcionário \n' +
                           '2 - Consultar Funcionário(s) \n' +
                           '3 - Remover Funcionário \n' +
                           '4 - Sair \n' +
                           '>> ')
    if opcaoPrincipal == '1':
        codigoFuncionario = codigoFuncionario + 1
        cadastrarFuncionario(codigoFuncionario)
    elif opcaoPrincipal == '2':
        consultarFuncionario()
    elif opcaoPrincipal == '3':
        removerFuncionario()
    elif opcaoPrincipal == '4':
        break
    else:
        print('Opção Inválida...')
        continue
# Fim da Main
