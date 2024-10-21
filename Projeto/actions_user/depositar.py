from Projeto.actions_user.loadupload import load_users, update_user_data


# deposita valor
def mathdepositar(cpf):
    # pega o valor autal
    users = load_users('users.txt')
    saldo = 0

    deposito = float(input('Digite o valor do depósito: '))
    saldo = saldo + deposito



    for user in users:
        cpf2 = user['cpf']
        if cpf2 == str(cpf):
            print('cpf ==')
            update_user_data(cpf, saldo, user['bitcoin'], user['ethereum'], user['ripple'])

    print('O valor na sua carteira é de', saldo)

mathdepositar(12345678900)