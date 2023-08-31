# --------------- Início das Variáveis Globais ---------------
lista_colaborador = []
id_colaborador = 0
# --------------- Fim das Variáveis Globais ------------------



# --------------- Início de cadastrar_colaborador() ---------------
def cadastrar_colaborador(id):
    print('------------------------- MENU CADASTRAR COLABORADOR ------------------------- \n')
    print('ID do Colaborador: {}' .format(id))
    nome = input('Entre com o NOME do Colaborador: ')
    setor = input('Entre com o SETOR do Colaborador: ')
    pagamento = int(input('Entre com o PAGAMENTO(R$) do Colaborador: '))
    dicionario_colaborador = {'id'           :id,
                              'nome'         :nome,
                              'setor'        :setor,
                              'pagamento'    :pagamento}
    lista_colaborador.append(dicionario_colaborador.copy())
# --------------- Fim de cadastrar_colaborador() ------------------

# --------------- Início de consultar_colaborador() ---------------
def consultar_colaborador():
    print('------------------------- MENU CONSULTAR COLABORADOR ------------------------- \n')
    while True:
        opcao_consultar = input('\n Escolha a opção desejada: \n' +
                                '1 - Consultar TODOS os Colaboradores \n' +
                                '2 - Consultar Colaborador por ID \n' +
                                '3 - Consultar Colaborador(es) por SETOR \n' +
                                '4 - Retornar \n' +
                                '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção Consultar TODOS os Colaboradores')
            for colaborador in lista_colaborador:
                print('--------------')
                for key, value in colaborador.items():
                    print('{} : {}' .format(key, value))
                print('--------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção Consultar Colaborador por ID')
            valor_desejado = int(input('Entre com o ID desejado: '))
            for colaborador in lista_colaborador:
                if colaborador['id'] == valor_desejado:
                    print('--------------')
                    for key, value in colaborador.items():
                        print('{} : {}'.format(key, value))
                print('--------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção Consultar Colaborador(es) por SETOR')
            valor_desejado = input('Entre com o SETOR desejado: ')
            for colaborador in lista_colaborador:
                if colaborador['setor'] == valor_desejado:
                    print('--------------')
                    for key, value in colaborador.items():
                        print('{} : {}'.format(key, value))
                print('--------------')
        elif opcao_consultar == '4':
            return # sai da funcao consultar e volta pro Main
        else:
            print('Opção inválida. Tente novamente')
            continue # volta pro inicio do laco
# --------------- Fim de consultar_colaborador() ------------------


# --------------- Início de remover_colaborador() ---------------
def remover_colaborador():
    print('------------------------- MENU REMOVER COLABORADOR ------------------------- \n')
    valor_desejado = int(input('Digite o id do colaborador a ser removido: '))
    for colaborador in lista_colaborador:
        if colaborador['id'] == valor_desejado:
            lista_colaborador.remove(colaborador)
            print('Colaborador removido')
# --------------- Fim de remover_colaborador() ------------------


# --------------- Início MAIN ---------------
print('Bem-vindo ao Controle de Colaboradores de Eduardo Vieira de Souza Cruz')
while True:
    opcao_principal = input('------------------------- MENU PRINCIPAL ------------------------- \n' +
                            'Escolha a opção desejada: \n' +
                            '1 - Cadastrar Colaborador \n' +
                            '2 - Consultar Colaborador(es) \n' +
                            '3 - Remover Colaborador \n' +
                            '4 - Sair \n' +
                            '>>')
    if opcao_principal == '1':
        id_colaborador = id_colaborador + 1
        cadastrar_colaborador(id_colaborador)
    elif opcao_principal == '2':
        consultar_colaborador()
    elif opcao_principal == '3':
        remover_colaborador()
    elif opcao_principal == '4':
        break
    else:
        print('Opçao inválida. Tente novamente')
        continue

# --------------- Fim MAIN ------------------