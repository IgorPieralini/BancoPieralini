from Projeto.UserUI.actions_user.ConfigUser import gerar_extrato


def mathsacar(user_config, cpf):
    """Função para sacar um valor da conta do usuário."""
    # Não criamos uma nova instância. Reutilizamos a instância passada.
    global valor
    if user_config.select_user_by_cpf(cpf):
        valor = float(input("Digite o valor para saque: "))

        if user_config.selected_user['saldo'] >= valor:
            user_config.selected_user['saldo'] -= valor  # Atualiza o saldo
            print(f"Saque de {valor} realizado com sucesso!")

            # Salva as alterações no arquivo
            user_config.salvar_users()
        else:
            print("Saldo insuficiente.")
    else:
        print("Usuário não encontrado.")

    gerar_extrato(user_config.selected_user, valor, 'REAL', 'saque')