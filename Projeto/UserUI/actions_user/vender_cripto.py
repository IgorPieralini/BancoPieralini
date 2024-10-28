from Projeto.UserUI.actions_user.ConfigUser import adicionar_extrato


def mathvender_cripto(user_config, cpf_user):
    """Permite ao usuário vender criptomoedas e registra no extrato."""
    print('1 - Vender Bitcoin')
    print('2 - Vender Ethereum')
    print('3 - Vender Ripple')

    try:
        resposta = int(input('Escolha a criptomoeda que deseja vender: '))
        valor = float(input('Digite o valor para venda: '))

        if resposta == 1:
            if valor <= user_config.selected_user['bitcoin']:
                user_config.selected_user['bitcoin'] -= valor
                adicionar_extrato(user_config.selected_user, valor, 'venda', 'BTC')
                print(f"Venda de {valor} BTC realizada com sucesso!")
            else:
                print("Saldo insuficiente de Bitcoin para a venda.")

        elif resposta == 2:
            if valor <= user_config.selected_user['ethereum']:
                user_config.selected_user['ethereum'] -= valor
                adicionar_extrato(user_config.selected_user, valor, 'venda', 'ETH')
                print(f"Venda de {valor} ETH realizada com sucesso!")
            else:
                print("Saldo insuficiente de Ethereum para a venda.")

        elif resposta == 3:
            if valor <= user_config.selected_user['ripple']:
                user_config.selected_user['ripple'] -= valor
                adicionar_extrato(user_config.selected_user, valor, 'venda', 'XRP')
                print(f"Venda de {valor} XRP realizada com sucesso!")
            else:
                print("Saldo insuficiente de Ripple para a venda.")

        else:
            print('Resposta inválida, tente novamente!')

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
bitcoin = 500
ripple = 500
ethereum = 500


def vender_bitcoin(user_config, cpf):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos bitcoins deseja vender: "))

        if int(user_config.selected_user['bitcoin']) < 0 :
            print('Você não tem saldo para isto')
        else:
            valor = quantidade_cripto * bitcoin
            user_config.selected_user['saldo'] += valor - (valor * 0.03) # Atualiza o saldo do usuário
            user_config.selected_user['bitcoin'] -= valor
            print(f"Você vendeu R$:{valor} de bitcoins!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")


def vender_ethereum(user_config, cpf):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos ethereums deseja vender: "))

        if int(user_config.selected_user['ethereum']) < 0 :
            print('Você não tem saldo para isto')
        else:
            valor = quantidade_cripto * bitcoin
            user_config.selected_user['saldo'] += valor - (valor * 0.02)  # Atualiza o saldo do usuário
            user_config.selected_user['ethereum'] -= valor
            print(f"Você vendeu R$:{valor} de ethereums!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")


def vender_ripple(user_config, cpf):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos ripples deseja vender: "))

        if int(user_config.selected_user['ripple']) < 0 :
            print('Você não tem saldo para isto')
        else:
            valor = quantidade_cripto * bitcoin
            user_config.selected_user['saldo'] += valor - (valor * 0.01)  # Atualiza o saldo do usuário
            user_config.selected_user['ripple'] -= valor
            print(f"Você vendeu R$:{valor} de ripples!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")