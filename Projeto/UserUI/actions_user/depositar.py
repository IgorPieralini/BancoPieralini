from Projeto.UserUI.actions_user.ConfigUser import gerar_extrato


def mathdepositar(user_config, cpf):
    global valor
    if user_config.select_user_by_cpf(cpf):
        valor = float(input("Digite o valor para depósito: "))
        user_config.selected_user['saldo'] += valor
        print(f"Depósito de {valor} realizado com sucesso!")

        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")

    gerar_extrato(user_config.selected_user, valor, 'REAL', 'deposito')

