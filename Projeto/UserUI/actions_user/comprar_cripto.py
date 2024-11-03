from Projeto.UserUI.actions_user.ConfigUser import adicionar_extrato


def mathcomprar_cripto(user_config, cpf_user, caminho):
    print('1 - Comprar Bitcoin')
    print('2 - Comprar Ethereum')
    print('3 - Comprar Ripple')

    try:
        resposta = int(input('Escolha a criptomoeda que deseja comprar: '))

        if resposta == 1:
            comprar_bitcoin(user_config, cpf_user, caminho)
        elif resposta == 2:
            comprar_ethereum(user_config, cpf_user, caminho)
        elif resposta == 3:
            comprar_ripple(user_config, cpf_user, caminho)
        else:
            print('Resposta inválida, tente novamente!')

        user_config.salvar_users()

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")


def comprar_bitcoin(user_config, cpf, caminho):
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()
    valores = linha.split(',')
    bitcoin_cotacao = int(valores[0])

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos bitcoins deseja comprar: "))
        valor_total = (quantidade_cripto * bitcoin_cotacao) * 1.02

        if valor_total > user_config.selected_user['saldo']:
            print('Você não tem saldo suficiente.')
        else:
            user_config.selected_user['saldo'] -= valor_total
            user_config.selected_user['bitcoin'] += quantidade_cripto
            adicionar_extrato(user_config.selected_user, quantidade_cripto, 'compra', 'BTC')
            print(f"Você comprou {quantidade_cripto} bitcoins!")
    else:
        print("Usuário não encontrado.")


def comprar_ethereum(user_config, cpf, caminho):
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()
    valores = linha.split(',')
    ethereum_cotacao = int(valores[1])

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos ethereums deseja comprar: "))
        valor_total = (quantidade_cripto * ethereum_cotacao) * 1.01

        if valor_total > user_config.selected_user['saldo']:
            print('Você não tem saldo suficiente.')
        else:
            user_config.selected_user['saldo'] -= valor_total
            user_config.selected_user['ethereum'] += quantidade_cripto
            adicionar_extrato(user_config.selected_user, quantidade_cripto, 'compra', 'ETH')
            print(f"Você comprou {quantidade_cripto} ethereums!")
    else:
        print("Usuário não encontrado.")


def comprar_ripple(user_config, cpf, caminho):
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()
    valores = linha.split(',')
    ripple_cotacao = int(valores[2])

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos ripples deseja comprar: "))
        valor_total = (quantidade_cripto * ripple_cotacao) * 1.01

        if valor_total > user_config.selected_user['saldo']:
            print('Você não tem saldo suficiente.')
        else:
            user_config.selected_user['saldo'] -= valor_total
            user_config.selected_user['ripple'] += quantidade_cripto
            adicionar_extrato(user_config.selected_user, quantidade_cripto, 'compra', 'XRP')
            print(f"Você comprou {quantidade_cripto} ripples!")

    else:
        print("Usuário não encontrado.")
