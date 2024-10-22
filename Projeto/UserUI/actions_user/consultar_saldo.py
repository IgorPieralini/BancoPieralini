
# consulta o saldo
def methconsultar_saldo(user_config, cpf):
    """Consulta o saldo do usuário logado."""
    if user_config.select_user_by_cpf(cpf):
        # Acessa e imprime os atributos do usuário selecionado
        print(f"Saldo: {user_config.saldo}")
        print(f"Bitcoin: {user_config.bitcoin}")
        print(f"Ethereum: {user_config.ethereum}")
        print(f"Ripple: {user_config.ripple}")
    else:
        print("Não foi possível selecionar o usuário.")