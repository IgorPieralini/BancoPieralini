from Projeto.actions_user import consultar_saldo
from Projeto.actions_user import atualizar_cotacao
from Projeto.actions_user import comprar_cripto
from Projeto.actions_user import consultar_extrato
from Projeto.actions_user import depositar
from Projeto.actions_user import sacar
from Projeto.actions_user import sair
from Projeto.actions_user import vender_cripto
from Projeto.actions_user.sair import mathsair
from Projeto.actions_user.loadupload import load_users





def mainUserInterface():
    logado = False

    # Se o usuário não estiver logado, realiza o login
    if not logado:

        users = load_users('database/users.txt')  # Carrega os usuários

        cpf_user = input('Digite seu CPF: ').strip()
        password_user = input('Digite sua senha: ').strip()

        # Itera sobre a lista de usuários e verifica as credenciais
        for user in users:
            if isinstance(user, dict):  # Verifica se é um dicionário válido
                if user['cpf'] == cpf_user and user['password'] == password_user:
                    print('------------------------------------------------------')
                    print('Nome:', user['name'])
                    print('CPF:', user['cpf'])
                    print()
                    logado = True  # Marca como logado
                    break  # Interrompe o loop se o login foi bem-sucedido
                else:
                    print('Login inválido encerrando programa')
                    mathsair()

        consultar_saldo.methconsultar_saldo()

        # Logaodo, enqaunto o usuario nao quiser sair
        while True:
            print('------------------------------------------------------')
            print('1.  Consultar saldo')
            print('2.  Consultar extrato')
            print('3.  Depositar')
            print('4.  Sacar')
            print('5.  Comprar criptomoedas')
            print('6.  Vender criptomoedas')
            print('7.  Atualizar cotação')
            print('8.  Sair')

            user_options = {
                1: consultar_saldo.methconsultar_saldo,
                2: consultar_extrato.mathconsultar_extrato,
                3: depositar.mathdepositar,
                4: sacar.mathsacar,
                5: comprar_cripto.mathcomprar_cripto,
                6: vender_cripto.mathvender_cripto,
                7: atualizar_cotacao.mathatualizar_cotacao,
                8: sair.mathsair
            }

            opcao = int(input())

            if opcao in user_options:
                user_options[opcao]()
            else:
                print('Opção inválida, tente novamente por gentileza')

    else:
        print('Login inválido! Tente novamente')
        if not logado:
            print("CPF ou senha incorretos. Tente novamente.")




