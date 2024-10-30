from Projeto.UserUI.actions_user.ConfigUser import adicionar_extrato



def mathvender_cripto(user_config, cpf_user, caminho):
    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()  # Ler a linha e remover espaços e quebras de linha

    # Separar os valores e convertê-los para inteiros
    valores = linha.split(',')
    bitcoin_cotacao, ethereum_cotacao, ripple_cotacao = int(valores[0]), int(valores[1]), int(valores[2])
    """Permite ao usuário vender criptomoedas e registra no extrato."""
    print('1 - Vender Bitcoin')
    print('2 - Vender Ethereum')
    print('3 - Vender Ripple')

    with open(caminho, 'r') as arquivo:
        linha = arquivo.readline().strip()  # Ler a linha e remover espaços e quebras de linha

    # Separar os valores e convertê-los para inteiros
    valores = linha.split(',')
    valor1, valor2, valor3 = int(valores[0]), int(valores[1]), int(valores[2])

    def mathatualizar_cotacao():
        with open('cotacao', 'r') as arquivo:
            linha = arquivo.readline().strip()  # Ler a linha e remover espaços e quebras de linha

        # Separar os valores pela vírgula
        valores = linha.split(',')

        # Armazenar cada valor em variáveis separadas, convertendo para inteiro
        bitcoin_cotacao = int(valores[0])
        ethereum_cotacao = int(valores[1])
        ripple_cotacao = int(valores[2])
    try:
        resposta = int(input('Escolha a criptomoeda que deseja vender: '))

        if resposta == 1:
            if user_config.select_user_by_cpf(cpf_user):
                quantidade_cripto = float(input("Digite quantos bitcoins deseja vender: "))
                valor = quantidade_cripto
                if int(user_config.selected_user['bitcoin']) < 0:
                    print('Você não tem saldo para isto')
                else:
                    if (valor * bitcoin_cotacao) > int(user_config.selected_user['bitcoin']):

                        user_config.selected_user['saldo'] += valor - (valor * 0.03)  # Atualiza o saldo do usuário
                        user_config.selected_user['bitcoin'] -= valor
                        adicionar_extrato(user_config.selected_user, valor, 'venda', 'BTC')
                        print(f"Você vendeu R$:{valor} de bitcoins!")

                # Salva as alterações no arquivo de usuários
                user_config.salvar_users()

        elif resposta == 2:
            if user_config.select_user_by_cpf(cpf_user):
                quantidade_cripto = float(input("Digite quantos ethereums deseja vender: "))

                if int(user_config.selected_user['ethereum']) < 0:
                    print('Você não tem saldo para isto')
                else:
                    valor = quantidade_cripto
                    if (valor * ethereum_cotacao) > int(user_config.selected_user['ethereum']):
                        user_config.selected_user['saldo'] += valor - (valor * 0.02)  # Atualiza o saldo do usuário
                        user_config.selected_user['ethereum'] -= valor
                        adicionar_extrato(user_config.selected_user, valor, 'venda', 'ETH')
                        print(f"Você vendeu R$:{valor} de ethereums!")

                # Salva as alterações no arquivo de usuários
                user_config.salvar_users()

        elif resposta == 3:
            if user_config.select_user_by_cpf(cpf_user):
                quantidade_cripto = float(input("Digite quantos ripples deseja vender: "))

                if int(user_config.selected_user['ripple']) < 0:
                    print('Você não tem saldo para isto')
                else:
                    valor = quantidade_cripto
                    if (valor * ripple_cotacao) > int(user_config.selected_user['ripple']):
                        user_config.selected_user['saldo'] += valor - (valor * 0.01)  # Atualiza o saldo do usuário
                        user_config.selected_user['ripple'] -= valor
                        adicionar_extrato(user_config.selected_user, valor, 'venda', 'XRP')
                        print(f"Você vendeu R$:{valor} de ripples!")

                # Salva as alterações no arquivo de usuários
                user_config.salvar_users()
            else:
                print("Usuário não encontrado.")

        else:
            print('Resposta inválida, tente novamente!')

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
