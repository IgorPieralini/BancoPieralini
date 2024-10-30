from Projeto.UserUI.actions_user.ConfigUser import adicionar_extrato


def mathcomprar_cripto(user_config, cpf_user, caminho):
    """Permite ao usuário comprar criptomoedas e registra no extrato."""
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

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

def comprar_bitcoin(user_config, cpf, caminho):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()  # Ler a linha e remover espaços e quebras de linha

    # Separar os valores e convertê-los para inteiros
    valores = linha.split(',')
    bitcoin_cotacao, ethereum_cotacao, ripple_cotacao = int(valores[0]), int(valores[1]), int(valores[2])
    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos bitcoins deseja comprar: "))
        valor = quantidade_cripto

        if (valor * bitcoin_cotacao) + ((valor * bitcoin_cotacao) * 0.02)  > int(user_config.selected_user['saldo']):
            print('Você não tem saldo para isto')
        else:
            user_config.selected_user['saldo'] -= (valor * bitcoin_cotacao) + ((valor * bitcoin_cotacao)  * 0.02)  # Atualiza o saldo do usuário
            user_config.selected_user['bitcoin'] += (valor * bitcoin_cotacao)
            adicionar_extrato(user_config.selected_user, valor, 'compra', 'BTC')
            print(f"Você comprou {valor} de bitcoins!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")

def comprar_ethereum(user_config, cpf, caminho):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()  # Ler a linha e remover espaços e quebras de linha

    # Separar os valores e convertê-los para inteiros
    valores = linha.split(',')
    bitcoin_cotacao, ethereum_cotacao, ripple_cotacao = int(valores[0]), int(valores[1]), int(valores[2])
    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos ethereums deseja comprar: "))
        valor = quantidade_cripto

        if (valor * ethereum_cotacao) + ((valor * ethereum_cotacao)* 0.01) >  int(user_config.selected_user['saldo']):
            print('Você não tem saldo para isto')
        else:
            user_config.selected_user['saldo'] -= (valor * ethereum_cotacao) + ((valor * ethereum_cotacao) * 0.01)   # Atualiza o saldo do usuário
            user_config.selected_user['ethereum'] += (valor * ethereum_cotacao)
            adicionar_extrato(user_config.selected_user, valor, 'compra', 'ETH')
            print(f"Você comprou {valor} de ethereums!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")

def comprar_ripple(user_config, cpf, caminho):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()  # Ler a linha e remover espaços e quebras de linha

    # Separar os valores e convertê-los para inteiros
    valores = linha.split(',')
    bitcoin_cotacao, ethereum_cotacao, ripple_cotacao = int(valores[0]), int(valores[1]), int(valores[2])
    if user_config.select_user_by_cpf(cpf):
        quantidade_cripto = float(input("Digite quantos ripples deseja comprar: "))
        valor = quantidade_cripto

        if (valor * ripple_cotacao) + ((valor * ripple_cotacao) * 0.01)  > int(user_config.selected_user['saldo']):
            print('Você não tem saldo para isto')
        else:
            user_config.selected_user['saldo'] -= (valor * ripple_cotacao) + ((valor * ripple_cotacao) * 0.01)   # Atualiza o saldo do usuário
            user_config.selected_user['ripple'] += (valor * ripple_cotacao)
            adicionar_extrato(user_config.selected_user, valor, 'compra', 'XRP')
            print(f"Você comprou {valor} de ripples!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")