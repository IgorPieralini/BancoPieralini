def methconsultar_saldo(user_config, cpf):
    if user_config.select_user_by_cpf(cpf):
        print(f"Carteira: {user_config.saldo}")
        print(f"Bitcoins: {user_config.bitcoin}")
        print(f"Ethereums: {user_config.ethereum}")
        print(f"Ripples: {user_config.ripple}")
    else:
        print("Impossível de selecionar Usuário.")