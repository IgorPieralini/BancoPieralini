from Projeto.UserUI.actions_user.ConfigUser import adicionar_extrato


def mathcomprar_cripto(user_config, cpf_user):
    """Permite ao usuário comprar criptomoedas e registra no extrato."""
    print('1 - Comprar Bitcoin')
    print('2 - Comprar Ethereum')
    print('3 - Comprar Ripple')

    try:
        resposta = int(input('Escolha a criptomoeda que deseja comprar: '))

        if resposta == 1:
            comprar_bitcoin(user_config, cpf_user)
        elif resposta == 2:
            comprar_ethereum(user_config, cpf_user)
        elif resposta == 3:
            comprar_ripple(user_config, cpf_user)
        else:
            print('Resposta inválida, tente novamente!')

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

bitcoin = 500
ripple = 500
ethereum = 500

def comprar_bitcoin(user_config, cpf):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos bitcoins deseja comprar: "))
        valor = quantidade_cripto

        if valor + (valor * 0.02)  > int(user_config.selected_user['saldo']):
            print('Você não tem saldo para isto')
        else:
            user_config.selected_user['saldo'] -= valor + (valor * 0.02)  # Atualiza o saldo do usuário
            user_config.selected_user['bitcoin'] += valor
            adicionar_extrato(user_config.selected_user, valor, 'compra', 'BTC')
            print(f"Você comprou R$:{valor} de bitcoins!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")

def comprar_ethereum(user_config, cpf):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos ethereums deseja comprar: "))
        valor = quantidade_cripto

        if valor + (valor * 0.01) >  int(user_config.selected_user['saldo']):
            print('Você não tem saldo para isto')
        else:
            user_config.selected_user['saldo'] -= valor + (valor * 0.01)   # Atualiza o saldo do usuário
            user_config.selected_user['ethereum'] += valor
            adicionar_extrato(user_config.selected_user, valor, 'compra', 'ETH')
            print(f"Você comprou R$:{valor} de ethereums!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")

def comprar_ripple(user_config, cpf):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.

    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos ripples deseja comprar: "))
        valor = quantidade_cripto

        if valor + (valor * 0.01)   > int(user_config.selected_user['saldo']):
            print('Você não tem saldo para isto')
        else:
            user_config.selected_user['saldo'] -= valor + (valor * 0.01)   # Atualiza o saldo do usuário
            user_config.selected_user['ripple'] += valor
            adicionar_extrato(user_config.selected_user, valor, 'compra', 'XRP')
            print(f"Você comprou R$:{valor} de ripples!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")