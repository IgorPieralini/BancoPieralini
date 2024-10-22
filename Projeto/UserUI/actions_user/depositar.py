def mathdepositar(user_config, cpf):
    """Função para depositar um valor na conta do usuário."""
    # A instância de user_config já está sendo passada corretamente, não precisa criar uma nova.

    if user_config.select_user_by_cpf(cpf):
        valor = float(input("Digite o valor para depósito: "))
        user_config.selected_user['saldo'] += valor  # Atualiza o saldo do usuário
        print(f"Depósito de {valor} realizado com sucesso!")

        # Salva as alterações no arquivo de usuários
        user_config.salvar_users()
    else:
        print("Usuário não encontrado.")